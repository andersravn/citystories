# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20151001_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='type',
            field=models.CharField(editable=False, default='note', max_length=4),
        ),
        migrations.AddField(
            model_name='userentry',
            name='type',
            field=models.CharField(editable=False, default='userentry', max_length=9),
        ),
    ]
