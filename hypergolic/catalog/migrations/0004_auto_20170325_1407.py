# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_compound_abbreviation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compound',
            name='chem_formula',
            field=models.CharField(max_length=30, null=True),
        ),
    ]