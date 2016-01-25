# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20160121_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='place',
            field=models.CharField(max_length=55, null=True, blank=True),
        ),
    ]
