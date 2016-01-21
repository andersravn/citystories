 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

import uuid

from django.utils import timezone
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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
    pnt = models.PointField(null=True, blank=True, geography=True)
    objects = models.GeoManager()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text_content


class UserEntry(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=9, default='userentry', editable=False)
    user = models.ForeignKey(User, null=True, blank=True)
    text_content = models.TextField()
    rating = models.IntegerField(default=1)
    lat = models.CharField(max_length=20, null=True, blank=True)
    lng = models.CharField(max_length=20, null=True, blank=True)
    pnt = models.PointField(null=True, blank=True, geography=True)
    no_good = models.BooleanField(default=False)
    objects = models.GeoManager()
    created = models.DateTimeField(default=timezone.now, editable=False)

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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=4, default='note', editable=False)
    note_id = models.CharField(max_length=25)
    text_content = models.TextField()
    note_type = models.CharField(max_length=10)
    from_date = models.DateField()
    media = models.BooleanField(default=False)
    no_good = models.BooleanField(default=False)
    lat = models.CharField(max_length=12, default='none')
    lng = models.CharField(max_length=12, default='none')
    place = models.ForeignKey(Place)
    pnt = models.PointField(null=True, blank=True, geography=True)
    rating = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    last_changed = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.place.name + ' | ' + str(self.from_date)


class DfiFilm(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=4, default='film', editable=False)
    title = models.CharField(max_length=100)
    text_content = models.TextField()
    rating = models.IntegerField(default=1)
    duration = models.IntegerField(blank=True)
    embed = models.TextField()
    lat = models.CharField(max_length=12, default='none')
    long = models.CharField(max_length=12, default='none')
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class NoteVote(models.Model):
    user = models.ForeignKey(User)
    note = models.ForeignKey(Note)
    value = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + str(self.note.uuid)


class UserentryVote(models.Model):
    user = models.ForeignKey(User)
    userentry = models.ForeignKey(UserEntry)
    value = models.SmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " - " + str(self.userentry.uuid)


class LatestPlace(models.Model):
    placeid = models.IntegerField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
