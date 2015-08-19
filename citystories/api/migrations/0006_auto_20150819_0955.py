# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_testentry_pnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testentry',
            name='pnt',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True),
        ),
    ]
