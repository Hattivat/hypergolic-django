# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 00:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20170325_2340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Engine role', 'verbose_name_plural': 'Engine role'},
        ),
    ]