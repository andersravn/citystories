#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.gis import admin
from api.models import Place, Note, TestEntry, UserEntry, DfiFilm, NoteVote, UserentryVote

# Register your models here.

admin.site.register(Place)
admin.site.register(Note)
admin.site.register(UserEntry, admin.GeoModelAdmin)
admin.site.register(TestEntry, admin.GeoModelAdmin)
admin.site.register(DfiFilm)
admin.site.register(NoteVote)
admin.site.register(UserentryVote)
