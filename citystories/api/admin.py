from django.contrib import admin
from api.models import Entry, Place, Note, TestEntry

# Register your models here.

admin.site.register(Entry)
admin.site.register(Place)
admin.site.register(Note)
admin.site.register(TestEntry)
