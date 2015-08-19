 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.contrib.gis import admin
from api.models import Entry, Place, Note, TestEntry

# Register your models here.

admin.site.register(Entry)
admin.site.register(Place)
admin.site.register(Note)
admin.site.register(TestEntry, admin.GeoModelAdmin)
