# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20161113_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendoritem',
            options={'ordering': ['name', 'code'], 'verbose_name': 'Vendor Item', 'verbose_name_plural': 'Vendor Items'},
        ),
        migrations.AlterModelOptions(
            name='vendorvariant',
            options={'ordering': ['name', 'code'], 'verbose_name': 'Vendor Variant', 'verbose_name_plural': 'Vendor Variants'},
        ),
        migrations.AddField(
            model_name='vendoritem',
            name='dt_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vendoritem',
            name='dt_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='vendoritem',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active?'),
        ),
        migrations.AddField(
            model_name='vendoritem',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Manufacturer'),
        ),
        migrations.AddField(
            model_name='vendorvariant',
            name='dt_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='vendorvariant',
            name='dt_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='vendorvariant',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is Active?'),
        ),
    ]
