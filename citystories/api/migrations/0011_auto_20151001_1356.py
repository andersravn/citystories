# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20150929_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userentry',
            name='id',
        ),
        migrations.AddField(
            model_name='note',
            name='uuid',
            field=models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False),
        ),
        migrations.AddField(
            model_name='userentry',
            name='uuid',
            field=models.UUIDField(serialize=False, default=uuid.uuid4, primary_key=True, editable=False),
        ),
    ]
