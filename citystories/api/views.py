#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import chain

from django.shortcuts import render
from django.contrib.gis.geos import fromstr
from django.core.exceptions import MultipleObjectsReturned

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_auth.registration.views import LoginView
from drf_multiple_model.views import MultipleModelAPIView

from .serializers import UserEntrySerializer, LimitedUserEntrySerializer, NoteSerializer, LimitedNoteSerializer, \
    DfiFilmSerializer, UserVoteSerializer
from .models import UserEntry, Note, DfiFilm, NoteVote, UserentryVote

from .utils import get_address


def front_view(request):
    context = {}
    template_name = 'api/front.html'

    if request.method == 'GET':
        return render(request, template_name, context)


class AllDataLessThanView(MultipleModelAPIView):
    flat = True
    sorting_field = 'rating'

    def get_queryList(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        distance = self.kwargs['distance']
        pnt = fromstr('POINT(' + lon + ' ' + lat + ')', srid=4326)

        queryList = [
            (UserEntry.objects.filter(no_good=False, pnt__distance_lte=(pnt, int(distance))), UserEntrySerializer),
            (Note.objects.filter(no_good=False, pnt__distance_lte=(pnt, int(distance))), NoteSerializer),
        ]
        return queryList


class AllDataGreaterThanView(MultipleModelAPIView):
    flat = True
    sorting_field = 'rating'

    def get_queryList(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        distance = self.kwargs['distance']
        pnt = fromstr('POINT(' + lon + ' ' + lat + ')', srid=4326)

        queryList = [
            (UserEntry.objects.filter(no_good=False, pnt__distance_gt=(pnt, int(distance))), LimitedUserEntrySerializer),
            (Note.objects.filter(no_good=False, pnt__distance_gt=(pnt, int(distance))), LimitedNoteSerializer),
        ]
        return queryList


class UserVotes(generics.ListAPIView):
    serializer_class = UserVoteSerializer

    def get_queryset(self):
        userentryvotes = UserentryVote.objects.filter(user=self.request.user)
        notevotes = NoteVote.objects.filter(user=self.request.user)

        userentry_info = []
        note_info = []

        for i in range(0, userentryvotes.count()):
            entry = dict()
            entry['uuid'] = userentryvotes[i].userentry.uuid
            entry['value'] = userentryvotes[i].value
            userentry_info.append(entry)

        for i in range(0, notevotes.count()):
            note = dict()
            note['uuid'] = notevotes[i].note.uuid
            note['value'] = notevotes[i].value
            note_info.append(note)

        return list(chain(userentry_info, note_info))


class MyUserEntries(generics.ListAPIView):
    serializer_class = UserEntrySerializer

    def get_queryset(self):
        return UserEntry.objects.filter(user=self.request.user)


# USER ENTRIES
class UserEntryView(generics.ListAPIView):
    queryset = UserEntry.objects.all()
    serializer_class = UserEntrySerializer

    def get_queryset(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        distance = self.kwargs['distance']
        pnt = fromstr('POINT(' + lon + ' ' + lat + ')', srid=4326)
        return UserEntry.objects.filter(no_good=False, pnt__distance_lte=(pnt, int(distance)))


# For the map view, that needs all entries and entry creation.
class CreateUserEntryViewSet(generics.ListCreateAPIView):
    queryset = UserEntry.objects.filter(no_good=False)
    serializer_class = UserEntrySerializer

    def perform_create(self, serializer):
        place = get_address(str(self.request.data['lat']), str(self.request.data['lng']))
        serializer.save(user=self.request.user, place=place)


# NOTES #
class NoteView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        distance = self.kwargs['distance']
        pnt = fromstr('POINT(' + lon + ' ' + lat + ')', srid=4326)
        return Note.objects.filter(no_good=False, pnt__distance_lte=(pnt, int(distance))).order_by('-rating')


# For the map view, that needs all notes
class NoteMapView(generics.ListAPIView):
    queryset = Note.objects.filter(no_good=False)
    serializer_class = NoteSerializer


# DFI FILM #
class DfiFilmView(generics.ListAPIView):
    queryset = DfiFilm.objects.all()
    serializer_class = DfiFilmSerializer


@api_view(['POST'])
def upvote(request, info):
    if request.method == 'POST':
        # info from the request is 'uuid,type'
        info = info.split(',')

        # NOTE UPVOTE
        if info[1] == 'note':
            note = Note.objects.get(pk=info[0])
            try:  # Try to find existing vote for the given note
                notevote = NoteVote.objects.get(user=request.user, note=note)
                if notevote.value == -1:  # If previous vote was negative
                    note.rating += 2  # Add two positive votes to compensate for negative vote
                    note.save()
                    notevote.value = 1  # Change the vote to a positive one
                    notevote.save()
                    return Response({"message": "upvoted"})
                elif notevote.value == 0:
                    note.rating += 1  # Add one positive vote
                    note.save()
                    notevote.value = 1  # Change the vote to a positive one
                    notevote.save()
                    return Response({"message": "upvoted"})
                elif notevote.value == 1:  # Unvote
                    note.rating -= 1
                    note.save()
                    notevote.value = 0  # Change to no vote
                    notevote.save()
                    return Response({"message": "unvoted"})
            except NoteVote.DoesNotExist:  # If no existing vote is found
                note.rating += 1
                note.save()
                notevote = NoteVote(user=request.user, note=note, value=1)  # Create the new vote
                notevote.save()
                return Response({"message": "upvoted"})
            except MultipleObjectsReturned:  # If there for some reason is more than one vote with the same user and note
                return Response({"message": "already_voted"})
            return Response({"message": "already_voted"})

        # USERENTRY UPVOTE
        if info[1] == 'userentry':
            userentry = UserEntry.objects.get(pk=info[0])
            try:
                userentryvote = UserentryVote.objects.get(user=request.user, userentry=userentry)
                if userentryvote.value == -1:  # If previous vote was negative
                    userentry.rating += 2  # Add two positive votes to compensate for negative vote
                    userentry.save()
                    userentryvote.value = 1  # Change the vote to a positive one
                    userentryvote.save()
                    return Response({"message": "upvoted"})
                elif userentryvote.value == 0:
                    userentry.rating += 1  # Add one positive vote
                    userentry.save()
                    userentryvote.value = 1  # Change the vote to a positive one
                    userentryvote.save()
                    return Response({"message": "upvoted"})
                elif userentryvote.value == 1:  # Unvote
                    userentry.rating -= 1
                    userentry.save()
                    userentryvote.value = 0  # Change to no vote
                    userentryvote.save()
                    return Response({"message": "unvoted"})
            except UserentryVote.DoesNotExist:  # If no existing vote is found
                userentry.rating += 1
                userentry.save()
                userentryvote = UserentryVote(user=request.user, userentry=userentry, value=1)  # Create the new vote
                userentryvote.save()
                return Response({"message": "upvoted"})
            except MultipleObjectsReturned:  # If there for some reason is more than one vote with the same user and note
                return Response({"message": "already_voted"})
            return Response({"message": "already_voted"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def downvote(request, info):
    if request.method == 'POST':
        # info from the request is 'uuid,type'
        info = info.split(',')

        # NOTE DOWNVOTE
        if info[1] == 'note':
            note = Note.objects.get(pk=info[0])
            try:  # Try to find existing vote for the given note
                notevote = NoteVote.objects.get(user=request.user, note=note)
                if notevote.value == 1:  # If previous vote was positive
                    note.rating -= 2  # Add two negative votes to compensate for positive vote
                    note.save()
                    notevote.value = -1  # Change the vote to a negative one
                    notevote.save()
                    return Response({"message": "downvoted"})
                elif notevote.value == 0:  # If previous vote was positive
                    note.rating -= 1  # Add one negative vote
                    note.save()
                    notevote.value = -1  # Change the vote to a negative one
                    notevote.save()
                    return Response({"message": "downvoted"})
                elif notevote.value == -1:  # Unvote
                    note.rating += 1
                    note.save()
                    notevote.value = 0  # Change to no vote
                    notevote.save()
                    return Response({"message": "unvoted"})
            except NoteVote.DoesNotExist:  # If no existing vote is found
                note.rating -= 1
                note.save()
                notevote = NoteVote(user=request.user, note=note, value=-1)  # Create the new vote
                notevote.save()
                return Response({"message": "downvoted"})
            except MultipleObjectsReturned:  # If there for some reason is more than one vote with the same user and note
                return Response({"message": "already_voted"})
            return Response({"message": "already_voted"})

        # USERENTRY DOWNVOTE
        if info[1] == 'userentry':
            userentry = UserEntry.objects.get(pk=info[0])
            try:
                userentryvote = UserentryVote.objects.get(user=request.user, userentry=userentry)
                if userentryvote.value == 1:  # If previous vote was positive
                    userentry.rating -= 2  # Add two negative votes to compensate for positive vote
                    userentry.save()
                    userentryvote.value = -1  # Change the vote to a negative one
                    userentryvote.save()
                    return Response({"message": "downvoted"})
                elif userentryvote.value == 0:  # If previous vote was positive
                    userentry.rating -= 1  # Add one negative vote
                    userentry.save()
                    userentryvote.value = -1  # Change the vote to a negative one
                    userentryvote.save()
                    return Response({"message": "downvoted"})
                elif userentryvote.value == -1:  # Unvote
                    userentry.rating += 1
                    userentry.save()
                    userentryvote.value = 0  # Change to no vote
                    userentryvote.save()
                    return Response({"message": "unvoted"})
            except UserentryVote.DoesNotExist:  # If no existing vote is found
                userentry.rating -= 1
                userentry.save()
                userentryvote = UserentryVote(user=request.user, userentry=userentry, value=-1)  # Create the new vote
                userentryvote.save()
                return Response({"message": "downvoted"})
            except MultipleObjectsReturned:  # If there for some reason is more than one vote with the same user and note
                return Response({"message": "already_voted"})
            return Response({"message": "already_voted"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def report(request, info):
    if request.method == 'POST':
        # info from the request is 'uuid,type'
        info = info.split(',')
        if info[1] == 'note':
            note = Note.objects.get(pk=info[0])
            note.reported = True
            note.save()
        if info[1] == 'userentry':
            userentry = UserEntry.objects.get(pk=info[0])
            userentry.reported = True
            userentry.save()
        return Response({"message": "Reported!"})
    return Response({"message": "Can not compute..."})
