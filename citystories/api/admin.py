 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.contrib.gis import admin
from api.models import Entry, Place, Note, TestEntry, UserEntry, DfiFilm

# Register your models here.

admin.site.register(Place)
admin.site.register(Note)
admin.site.register(UserEntry, admin.GeoModelAdmin)
admin.site.register(TestEntry, admin.GeoModelAdmin)
admin.site.register(DfiFilm)