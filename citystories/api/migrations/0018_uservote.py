# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0017_auto_20151221_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('notes', models.ManyToManyField(to='api.Note')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('userentries', models.ManyToManyField(to='api.UserEntry')),
            ],
        ),
    ]
