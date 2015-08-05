# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='LatestPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placeid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note_id', models.TextField()),
                ('text_content', models.TextField()),
                ('note_type', models.CharField(max_length=10)),
                ('from_date', models.DateField()),
                ('media', models.BooleanField(default=False)),
                ('no_good', models.BooleanField(default=False)),
                ('lat', models.CharField(default=b'none', max_length=12)),
                ('lng', models.CharField(default=b'none', max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('placeid', models.IntegerField()),
                ('name', models.CharField(max_length=55)),
                ('rank', models.IntegerField()),
                ('notes_loaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TestEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('lat', models.DecimalField(max_digits=17, decimal_places=14)),
                ('long', models.DecimalField(max_digits=17, decimal_places=14)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='place',
            field=models.ForeignKey(to='api.Place'),
        ),
    ]
