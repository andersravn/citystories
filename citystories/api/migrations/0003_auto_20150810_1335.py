# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150805_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testentry',
            old_name='content',
            new_name='text_content',
        ),
    ]
