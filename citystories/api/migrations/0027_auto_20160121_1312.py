# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20160121_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 21, 12, 12, 48, 942095, tzinfo=utc)),
        ),
    ]
