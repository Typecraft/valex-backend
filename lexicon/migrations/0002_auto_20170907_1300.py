# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 13:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lexicon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meaning',
            name='lemma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meanings', to='lexicon.Lemma'),
        ),
    ]
