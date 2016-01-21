# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0037_auto_20160121_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 12, 50, 41, 663345, tzinfo=utc), editable=False),
        ),
    ]
