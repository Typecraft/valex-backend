# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0008_auto_20170918_1538'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lemma',
            old_name='citation_form',
            new_name='citationForm',
        ),
    ]
