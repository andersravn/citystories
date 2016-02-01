 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import dashboard.scripts as scripts
from api.models import Place

# Create your views here.

from api.models import UserEntry, Note


def dash_view(request):
    context = {}
    template_name = 'dashboard/front.html'

    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, template_name, context)
        else:
            return redirect('/dash/login/')


@login_required(login_url='/dash/login/')
def userentry_reports_view(request):
    context = {}
    template_name = 'dashboard/userentry_reports.html'

    if request.method == 'GET':
        context['userentries'] = UserEntry.objects.filter(reported=True, no_good=False)
        return render(request, template_name, context)

    if request.method == 'POST':
        uuid = request.POST['uuid']
        userentry = UserEntry.objects.get(pk=uuid)
        if 'rm-userentry' in request.POST:
            userentry.no_good = True
            userentry.save()
        elif 'del-userentry' in request.POST:
            userentry.delete()
        return redirect('/dash/userentry-reports/')


@login_required(login_url='/dash/login/')
def note_reports_view(request):
    context = {}
    template_name = 'dashboard/note_reports.html'

    if request.method == 'GET':
        context['notes'] = Note.objects.filter(reported=True, no_good=False)
        return render(request, template_name, context)

    if request.method == 'POST':
        uuid = request.POST['uuid']
        note = Note.objects.get(pk=uuid)
        if 'rm-note' in request.POST:
            note.no_good = True
            note.save()
        elif 'del-note' in request.POST:
            note.delete()
        return redirect('/dash/note-reports/')


@login_required(login_url='/dash/login/')
def add_street_view(request):
    context = {}
    template_name = 'dashboard/add_street.html'

    if request.method == 'GET':
        return render(request, template_name, context)

    if request.method == 'POST':
        street = request.POST['street_name']
        loaded = scripts.add_street(street)  # Tilføjer sedler, og returnerer antal loadede/ikke loadede.
        messages.success(request, str(loaded) + ' sedler tilføjet.')
        return redirect('/dash/add-street/')


@login_required(login_url='/dash/login/')
def filter_view(request):
    context = {}
    template_name = 'dashboard/filter.html'

    if request.method == 'GET':
        return render(request, template_name, context)


@login_required(login_url='/dash/login/')
def stadsarkiv_api(request):
    context = {}
    template_name = 'dashboard/stadsarkiv_api.html'

    if request.method == 'GET':
        context['places'] = Place.objects.all()
        return render(request, template_name, context)


@login_required(login_url='/dash/login/')
def scripts_view(request):
    context = {}
    template_name = 'dashboard/scripts.html'

    if request.method == 'GET':
        return render(request, template_name, context)


@login_required(login_url='/dash/login/')
def load_csv(request):
    if request.method == 'GET':
        scripts.load_csv()  # Indsætter alle unikke steder i Sejrs Sedler.
        #scripts.get_notes()  # Henter data fra stadsarkivets api for hvert unikt steds id.
        #scripts.delete_duplicates()
        #scripts.add_coords()

        messages.success(request, 'Stederne er loaded i databasen!')
        return redirect('/dash/scripts/')


@login_required(login_url='/dash/login/')
def add_pnt_fields(request):
    if request.method == 'GET':
        scripts.add_pnt_fields() # Tilføjer pnt felter til alle Note objekter i databasen.

        messages.success(request, 'pnt felter er tilføjet')
        return redirect('/dash/scripts/')


def login_view(request):
    logout(request)
    context = {}
    template_name = 'dashboard/login.html'

    if request.method == 'GET':
        return render(request, template_name, context)


def auth_view(request):
    logout(request)
    username = request.POST.get('username', 'none')
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/dash/')
        else:
            return redirect('/dash/login/')
    else:
        return redirect('/dash/login/')


def logout_view(request):
    logout(request)
    return redirect('/dash/login/')
