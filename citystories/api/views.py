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
from .serializers import UserSerializer, UserEntrySerializer, NoteSerializer, DfiFilmSerializer
from .models import UserEntry, Note, DfiFilm


def front_view(request):
    context = {}
    template_name = 'api/front.html'

    if request.method == 'GET':
        return render(request, template_name, context)


# USER ENTRIES
class UserEntryView(generics.ListAPIView):
    queryset = UserEntry.objects.all()
    serializer_class = UserEntrySerializer

    def get_queryset(self):
        location = self.kwargs['location']
        pnt = fromstr('POINT(' + location + ')', srid=4326)
        return UserEntry.objects.filter(no_good=False, pnt__distance_lte=(pnt, 25))


# For the map view, that needs all entries.
class CreateUserEntryViewSet(generics.ListCreateAPIView):
    queryset = UserEntry.objects.filter(no_good=False)
    serializer_class = UserEntrySerializer


# NOTES #
class NoteView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        lat = self.kwargs['lat']
        lon = self.kwargs['lon']
        address = controllers.get_address(lat, lon)
        return Note.objects.filter(place__name=address, no_good=False).order_by('-rating')


# For the map view, that needs all entries
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
        if info[1] == 'note':
            note = Note.objects.get(pk=info[0])
            note.rating += 1
            note.save()
        if info[1] == 'userentry':
            userentry = UserEntry.objects.get(pk=info[0])
            userentry.rating += 1
            userentry.save()
        return Response({"message": "Upvoted!"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def downvote(request, info):
    if request.method == 'POST':
        # info from the request is 'uuid,type'
        info = info.split(',')
        if info[1] == 'note':
            note = Note.objects.get(pk=info[0])
            note.rating -= 1
            note.save()
        if info[1] == 'userentry':
            userentry = UserEntry.objects.get(pk=info[0])
            userentry.rating -= 1
            userentry.save()
        return Response({"message": "Downvoted!"})
    return Response({"message": "Can not compute..."})


@api_view(['POST'])
def report(request, info):
    if request.method == 'POST':
        # info from the request is 'uuid,type'
        info = info.split(',')
        if info[1] == 'note':
            note = Note.objects.get(pk=info[0])
            note.no_good = True
            note.save()
        if info[1] == 'userentry':
            userentry = UserEntry.objects.get(pk=info[0])
            userentry.no_good = True
            userentry.save()
        return Response({"message": "Reported!"})
    return Response({"message": "Can not compute..."})
