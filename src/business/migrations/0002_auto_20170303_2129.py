# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bzbrand',
            options={'ordering': ('-pk',), 'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='bzcreativecollection',
            options={'ordering': ('-pk',), 'verbose_name': 'Creative Collection', 'verbose_name_plural': 'Creative Collections'},
        ),
        migrations.AlterModelOptions(
            name='bzcreativedesign',
            options={'ordering': ('-pk',), 'verbose_name': 'Creative Design', 'verbose_name_plural': 'Creative Designs'},
        ),
        migrations.AlterModelOptions(
            name='bzcreativelayout',
            options={'ordering': ('-pk',), 'verbose_name': 'Creative Layout', 'verbose_name_plural': 'Creative Layouts'},
        ),
        migrations.AlterModelOptions(
            name='bzcreativerendering',
            options={'ordering': ('-pk',), 'verbose_name': 'Creative Rendering', 'verbose_name_plural': 'Creative Renderings'},
        ),
        migrations.AlterModelOptions(
            name='bzproduct',
            options={'ordering': ('-pk',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='bzproductvariant',
            options={'ordering': ('-pk',), 'verbose_name': 'Variant', 'verbose_name_plural': 'Variants'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogcolor',
            options={'ordering': ('-pk',), 'verbose_name': 'Printful Color', 'verbose_name_plural': 'Printful Colors'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogfilespec',
            options={'ordering': ('name',), 'verbose_name': 'Printful File Spec', 'verbose_name_plural': 'Printful File Specs'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogfiletype',
            options={'ordering': ('-pk',), 'verbose_name': 'Printful File Type', 'verbose_name_plural': 'Printful File Types'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogoptiontype',
            options={'ordering': ('-pk',), 'verbose_name': 'Printful Option Type', 'verbose_name_plural': 'Printful Option Types'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogproduct',
            options={'ordering': ('-pk',), 'verbose_name': 'Printful Product', 'verbose_name_plural': 'Printful Products'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogsize',
            options={'ordering': ('sort_group', 'sort_order'), 'verbose_name': 'Printful Size', 'verbose_name_plural': 'Printful Sizes'},
        ),
        migrations.AlterModelOptions(
            name='pfcatalogvariant',
            options={'ordering': ('-pk',), 'verbose_name': 'Printful Variant', 'verbose_name_plural': 'Printful Variants'},
        ),
        migrations.AlterModelOptions(
            name='pfcountry',
            options={'ordering': ('-pk',), 'verbose_name': 'Country', 'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='pfprintfile',
            options={'ordering': ('-created',), 'verbose_name': 'Printful File', 'verbose_name_plural': 'Printful Files'},
        ),
        migrations.AlterModelOptions(
            name='pfstate',
            options={'ordering': ('-pk',), 'verbose_name': 'State', 'verbose_name_plural': 'States'},
        ),
        migrations.AlterModelOptions(
            name='pfstore',
            options={'ordering': ('-created',), 'verbose_name': 'Printful Store', 'verbose_name_plural': 'Printful Stores'},
        ),
        migrations.AlterModelOptions(
            name='pfsyncitemoption',
            options={'ordering': ('-pk',), 'verbose_name': 'Sync Item Option', 'verbose_name_plural': 'Sync Item Options'},
        ),
        migrations.AlterModelOptions(
            name='pfsyncproduct',
            options={'ordering': ('-pk',), 'verbose_name': 'Sync Product', 'verbose_name_plural': 'Sync Products'},
        ),
        migrations.AlterModelOptions(
            name='pfsyncvariant',
            options={'ordering': ('-pk',), 'verbose_name': 'Sync Variant', 'verbose_name_plural': 'Sync Variants'},
        ),
        migrations.AlterModelOptions(
            name='wooattribute',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Attribute', 'verbose_name_plural': 'WP Attributes'},
        ),
        migrations.AlterModelOptions(
            name='woocategory',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Category', 'verbose_name_plural': 'WP Categories'},
        ),
        migrations.AlterModelOptions(
            name='wooimage',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Image', 'verbose_name_plural': 'WP Images'},
        ),
        migrations.AlterModelOptions(
            name='wooproduct',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Product', 'verbose_name_plural': 'WP Products'},
        ),
        migrations.AlterModelOptions(
            name='wooshippingclass',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Shipping Class', 'verbose_name_plural': 'WP Shipping Classes'},
        ),
        migrations.AlterModelOptions(
            name='woostore',
            options={'ordering': ('code',), 'verbose_name': 'WP Store', 'verbose_name_plural': 'WP Stores'},
        ),
        migrations.AlterModelOptions(
            name='wootag',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Tag', 'verbose_name_plural': 'WP Tags'},
        ),
        migrations.AlterModelOptions(
            name='wooterm',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Term', 'verbose_name_plural': 'WP Terms'},
        ),
        migrations.AlterModelOptions(
            name='woovariant',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Variant', 'verbose_name_plural': 'WP Variants'},
        ),
        migrations.AlterModelOptions(
            name='wpmedia',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Media', 'verbose_name_plural': 'WP Media'},
        ),
        migrations.AlterModelOptions(
            name='wpmediasize',
            options={'ordering': ('-pk',), 'verbose_name': 'WP Media Size', 'verbose_name_plural': 'WP Media Sizes'},
        ),
        migrations.AddField(
            model_name='bzbrand',
            name='outlet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='business.wooStore'),
        ),
        migrations.AlterField(
            model_name='pfcatalogvariant',
            name='is_active',
            field=models.BooleanField(default=True, help_text='', verbose_name='Is Active?'),
        ),
        migrations.AlterField(
            model_name='wooattribute',
            name='wid',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='woocategory',
            name='wid',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='wooimage',
            name='wid',
            field=models.CharField(blank=True, default='', help_text='Image ID (attachment ID). In write-mode used to attach pre-existing images.', max_length=16, null=True, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='wooproduct',
            name='wid',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='wooshippingclass',
            name='wid',
            field=models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='wootag',
            name='wid',
            field=models.IntegerField(default=0, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='wooterm',
            name='wid',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='WP ID'),
        ),
        migrations.AlterField(
            model_name='woovariant',
            name='wid',
            field=models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='WP ID'),
        ),
    ]
