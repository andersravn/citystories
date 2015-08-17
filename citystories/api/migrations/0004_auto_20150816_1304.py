# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150810_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='lat',
            field=models.CharField(default='none', max_length=12),
        ),
        migrations.AlterField(
            model_name='note',
            name='lng',
            field=models.CharField(default='none', max_length=12),
        ),
    ]
