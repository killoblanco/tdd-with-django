# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solo',
            name='artist',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='instument',
            field=models.CharField(default='n/a', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solo',
            name='track',
            field=models.CharField(default='n/a', max_length=100),
            preserve_default=False,
        ),
    ]
