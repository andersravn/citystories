# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_userentry_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='reported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userentry',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
