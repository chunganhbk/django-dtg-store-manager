# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-19 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outlet_woo', '0002_auto_20161117_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='design',
            field=models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_item_design', to='creative.Design'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(blank=True, help_text='', null=True, on_delete=django.db.models.deletion.CASCADE, to='outlet_woo.Shop'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='app_added',
            field=models.DateTimeField(auto_now_add=True, help_text=''),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='app_last_sync',
            field=models.DateTimeField(auto_now=True, help_text=''),
        ),
    ]