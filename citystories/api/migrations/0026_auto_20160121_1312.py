# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20160121_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 12, 12, 27, 353250, tzinfo=utc)),
        ),
    ]
