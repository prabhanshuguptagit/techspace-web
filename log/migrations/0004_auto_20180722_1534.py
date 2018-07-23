# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-22 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20180620_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='institution',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedIn',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='default/Default_avatar.jpg', upload_to='user/avatar/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year_of_graduation',
            field=models.IntegerField(choices=[(2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026), (2027, 2027)], default=2018, verbose_name='year'),
        ),
    ]