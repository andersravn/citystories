# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20160121_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userentry',
            name='created',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2016, 1, 21, 12, 46, 3, 112010, tzinfo=utc)),
        ),
    ]
