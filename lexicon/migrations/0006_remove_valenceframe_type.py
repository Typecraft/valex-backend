# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 06:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0005_valenceframe_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='valenceframe',
            name='type',
        ),
    ]
