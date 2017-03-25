# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20170325_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='variety_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='version', to='catalog.Compound'),
        ),
    ]
