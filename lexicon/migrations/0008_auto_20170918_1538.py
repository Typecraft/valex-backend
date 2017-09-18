# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0007_auto_20170918_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='lemma',
            name='citation_form',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lemma',
            name='comment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
