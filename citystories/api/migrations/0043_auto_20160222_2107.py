# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20160222_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lat',
            field=models.CharField(max_length=20, default='none'),
        ),
        migrations.AlterField(
            model_name='note',
            name='lng',
            field=models.CharField(max_length=20, default='none'),
        ),
    ]
