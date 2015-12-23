# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_uservote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uservote',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='userentries',
        ),
        migrations.DeleteModel(
            name='UserVote',
        ),
    ]
