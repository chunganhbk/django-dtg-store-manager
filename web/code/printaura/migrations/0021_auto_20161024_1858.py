# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printaura', '0020_auto_20161024_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='productvariant',
            name='image',
            field=models.ImageField(blank=True, height_field='image_height', null=True, upload_to='product/', verbose_name='Variant Image', width_field='image_width'),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image_height',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='image_width',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='productvariant',
            name='local_sku',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='web_url',
            field=models.URLField(blank=True, verbose_name='Website URL'),
        ),
    ]