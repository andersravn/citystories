# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_auto_20160121_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
