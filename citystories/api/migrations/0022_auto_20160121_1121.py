# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20160121_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 21, 11, 21, 46, 874332, tzinfo=utc)),
        ),
    ]
