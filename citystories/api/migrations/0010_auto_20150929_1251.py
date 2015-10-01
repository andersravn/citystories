# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20150903_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='lat',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='userentry',
            name='lng',
            field=models.CharField(null=True, max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='userentry',
            name='no_good',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userentry',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]
