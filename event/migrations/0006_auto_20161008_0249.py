# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-07 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20161008_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'События'},
        ),
    ]
