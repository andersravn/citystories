# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0044_auto_20160222_2126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='pnt',
        ),
    ]
