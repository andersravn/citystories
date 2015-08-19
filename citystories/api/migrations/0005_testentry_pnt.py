# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150816_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='testentry',
            name='pnt',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
    ]
