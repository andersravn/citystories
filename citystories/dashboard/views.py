 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import dashboard.scripts as scripts
from api.models import Place

# Create your views here.


def dash_view(request):
    context = {}
    template_name = 'dashboard/front.html'

    if request.method == 'GET':
        if request.user.is_authenticated():
            return render(request, template_name, context)
        else:
            return redirect('/dash/login/')


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


def stadsarkiv_api(request):
    context = {}
    template_name = 'dashboard/stadsarkiv_api.html'

    if request.method == 'GET':
        context['places'] = Place.objects.all()
        return render(request, template_name, context)


def scripts_view(request):
    context = {}
    template_name = 'dashboard/scripts.html'

    if request.method == 'GET':
        return render(request, template_name, context)


def load_csv(request):
    if request.method == 'GET':
        scripts.load_csv()  # Indsætter alle unikke steder i Sejrs Sedler.
        #scripts.get_notes()  # Henter data fra stadsarkivets api for hvert unikt steds id.
        #scripts.delete_duplicates()
        #scripts.add_coords()

        messages.success(request, 'Stederne er loaded i databasen!')
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
