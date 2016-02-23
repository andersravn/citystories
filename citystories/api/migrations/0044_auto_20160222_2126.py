# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0043_auto_20160222_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_id',
            field=models.CharField(max_length=30),
        ),
    ]
