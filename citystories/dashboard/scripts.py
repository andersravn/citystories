#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv, os, datetime, requests

from django.db import DataError

from api.models import Place, Note


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

# url = 'https://openaws.appspot.com/records?collection=1&locations=2670'
# response = urllib.urlopen(url)
# data = json.loads(response.read())


# Indsætter alle unikke steder i Sejrs Sedler.
def load_csv():
    Place.objects.all().delete()
    with open(os.path.dirname(os.path.abspath(__file__)) + '/sejrssedler_steder.csv', 'rt') as csvfile:
        notereader = csv.reader(csvfile, delimiter=',')
        firstline = True
        for row in notereader:
            if firstline:
                firstline = False
                continue
            p = Place(placeid=int(row[0]), name=row[1], rank=int(row[2]))
            p.save()


# Henter data fra stadsarkivets api for hvert unikt steds id.
# Hentede 11036 notes ved første run.
def get_notes(place):
    url = 'https://openaws.appspot.com/records?collection=1&locations='

    response = requests.get(url + str(place.placeid))
    data = response.json()
    note_type = ''
    loaded = 0

    # Tjekker om result objektet er tomt.
    try:
        data['result'][0]
    except IndexError:
        return

    for r in data['result']:
        if 'personalsedler' in r['description']['hierarchical_level'].lower():
            note_type = 'personal'
        else:
            note_type = 'emne'

        date = r['description'].get('from_date', '2017-01-01')
        year = date[:4]
        month = date[5:7]
        day = date[8:]
        analog_content = r.get('analog_content', 'none')
        media = False
        admin_data = r['administration'].get('admin_data', 'none')

        if admin_data is not 'none':
            media = admin_data.get('formidlingsegnet', 'none')

            if media is not 'none':
                media = r['administration']['admin_data']['formidlingsegnet']
            else:
                media = False

        # Tjekker efter fejlindtastning i måned.
        if month == '00':
            month = '01'

        # Tjekker efter fejlindtastning i dag.
        if day == '00':
            day = '01'

        if analog_content is not 'none':
            analog_content = r['analog_content']['storage_id']

        note = Note(note_id=analog_content,
                    text_content=r['description']['textcontent'],
                    note_type=note_type,
                    from_date=datetime.date(int(year), int(month), int(day)),
                    media=media,
                    place=place)
        note.save()
        loaded += 1
    return loaded


# 8494 tilbage efter første run.
def delete_duplicates():
    for row in Note.objects.all():
        if Note.objects.filter(note_id=row.note_id, note_type=row.note_type).count() > 1:
            row.delete()


def add_coords():
    notes = Note.objects.all()
    for note in notes:
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + note.place.name + ',+Aarhus,+Danmark')
        data = response.json()
        note.lat = data['results'][0]['geometry']['location']['lat']
        note.lng = data['results'][0]['geometry']['location']['lng']
        note.save()


def add_street(street):
    places = Place.objects.filter(name__contains=street)
    loaded = 0

    for place in places:
        loaded += get_notes(place)
        place.notes_loaded = True  # notes_loaded indikerer nu om der loaded koordinater på sedler knytter til et placeid
        place.save()
    return loaded
