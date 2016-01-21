# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20160121_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 12, 32, 54, 809887, tzinfo=utc), blank=True),
        ),
    ]
