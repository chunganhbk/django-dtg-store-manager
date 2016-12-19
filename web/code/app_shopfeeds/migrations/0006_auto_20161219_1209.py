# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shopfeeds', '0005_auto_20161216_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datafeed',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='datafeed',
            name='date_lastgenerated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]