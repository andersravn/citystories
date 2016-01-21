# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_auto_20160121_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(editable=False, default=django.utils.timezone.now),
        ),
    ]
