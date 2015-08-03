#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout

from rest_framework import permissions, viewsets, generics

from api import controllers

from .permissions import IsAuthorOrReadOnly
from .serializers import EntrySerializer, UserSerializer, NoteSerializer, TestEntrySerializer
from .models import Entry, Note, TestEntry


def front_view(request):
    context = {}
    template_name = 'api/front.html'

    if request.method == 'GET':
        return render(request, template_name, context)


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)

    def pre_save(self, obj):
        obj.user = self.request.user


class TestEntryViewSet(generics.ListCreateAPIView):
    queryset = TestEntry.objects.all()
    serializer_class = TestEntrySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteView(generics.ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        location = self.kwargs['location']
        address = controllers.get_address(location)
        return Note.objects.filter(place__name=address)
