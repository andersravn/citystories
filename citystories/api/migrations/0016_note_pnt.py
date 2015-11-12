# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='pnt',
            field=django.contrib.gis.db.models.fields.PointField(geography=True, blank=True, srid=4326, null=True),
        ),
    ]
