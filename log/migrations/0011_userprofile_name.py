# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-22 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0010_auto_20180818_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
