from django.contrib.gis.db import models
from django.contrib.auth.models import User

from .utils import haversine

# Create your models here.


class Entry(models.Model):
    content = models.CharField(max_length=25)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content


class TestEntry(models.Model):
    text_content = models.TextField()
    lat = models.DecimalField(max_digits=17, decimal_places=14)
    long = models.DecimalField(max_digits=17, decimal_places=14)
    pnt = models.PointField(null=True, blank=True)
    objects = models.GeoManager()
    created = models.DateTimeField(auto_now_add=True)

    def is_nearby(self, current_lat, current_long):
        return haversine(current_long, current_lat, self.long, self.lat) > 10

    def __str__(self):
        return self.text_content


class Place(models.Model):
    placeid = models.IntegerField()
    name = models.CharField(max_length=55)
    rank = models.IntegerField()
    notes_loaded = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Note(models.Model):
    note_id = models.CharField(max_length=25)
    text_content = models.TextField()
    note_type = models.CharField(max_length=10)
    from_date = models.DateField()
    media = models.BooleanField(default=False)
    no_good = models.BooleanField(default=False)
    lat = models.CharField(max_length=12, default='none')
    lng = models.CharField(max_length=12, default='none')
    place = models.ForeignKey(Place)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place.name + ' | ' + str(self.from_date)


class LatestPlace(models.Model):
    placeid = models.IntegerField()
