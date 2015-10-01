#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from django.contrib.gis.geos import fromstr

from rest_framework import permissions, viewsets, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api import controllers

from .permissions import IsAuthorOrReadOnly
from .serializers import UserSerializer, NoteSerializer, UserEntrySerializer
from .models import Note, UserEntry


def front_view(request):
    context = {}
    template_name = 'api/front.html'

    if request.method == 'GET':
        return render(request, template_name, context)


# USER ENTRIES
class UserEntryViewSet(generics.ListAPIView):
    queryset = UserEntry.objects.all()
    serializer_class = UserEntrySerializer

    def get_queryset(self):
        location = self.kwargs['location']
        pnt = fromstr('POINT(' + location + ')', srid=4326)
        return UserEntry.objects.filter(pnt__distance_lte=(pnt, 25))


# For the map view, that needs all entries.
class CreateUserEntryViewSet(generics.ListCreateAPIView):
    queryset = UserEntry.objects.all()
    serializer_class = UserEntrySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def upvote_userentry(request, note_id):
    if request.method == 'POST':
        note = UserEntry.objects.get(pk=note_id)
        note.rating += 1
        note.save()
        return Response({"message": "Upvoted!"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def downvote_userentry(request, note_id):
    if request.method == 'POST':
        note = UserEntry.objects.get(pk=note_id)
        note.rating -= 1
        note.save()
        return Response({"message": "Downvoted!"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def report_userentry(request, note_id):
    if request.method == 'POST':
        note = UserEntry.objects.get(pk=note_id)
        note.no_good = True
        note.save()
        return Response({"message": "Reported!"})
    return Response({"message": "Can not compute..."})


# NOTES #
class NoteView(generics.ListAPIView):
    queryset = Note.objects.filter()
    serializer_class = NoteSerializer

    def get_queryset(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        address = controllers.get_address(lat, lon)
        return Note.objects.filter(place__name=address, no_good=False).order_by('-rating')


class NoteMapView(generics.ListAPIView):
    queryset = Note.objects.filter(no_good=False)
    serializer_class = NoteSerializer


@api_view(['POST'])
def upvote_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        note.rating += 1
        note.save()
        return Response({"message": "Upvoted!"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def downvote_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        note.rating -= 1
        note.save()
        return Response({"message": "Downvoted!"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def report_note(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        note.no_good = True
        note.save()
        return Response({"message": "Reported!"})
    return Response({"message": "Can not compute..."})
