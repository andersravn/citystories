# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_note_changed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='changed',
            new_name='last_changed',
        ),
    ]
