# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20151001_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='DfiFilm',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False, default=uuid.uuid4, editable=False)),
                ('type', models.CharField(max_length=4, default='film', editable=False)),
                ('title', models.CharField(max_length=100)),
                ('text_content', models.TextField()),
                ('rating', models.IntegerField(default=1)),
                ('duration', models.IntegerField(blank=True)),
                ('embed', models.TextField()),
                ('lat', models.CharField(max_length=12, default='none')),
                ('long', models.CharField(max_length=12, default='none')),
                ('pnt', django.contrib.gis.db.models.fields.PointField(geography=True, blank=True, srid=4326, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
