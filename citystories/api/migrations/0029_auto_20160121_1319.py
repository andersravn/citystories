# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_auto_20160121_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 1, 21, 12, 19, 19, 475180, tzinfo=utc)),
        ),
    ]
