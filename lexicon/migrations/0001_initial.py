# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-07 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Lemma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lemma', models.CharField(max_length=255)),
                ('language', models.CharField(choices=[('nob', 'Norwegian'), ('deu', 'German')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.TextField()),
                ('ontologyToken', models.CharField(max_length=4)),
                ('lemma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.Lemma')),
            ],
        ),
        migrations.CreateModel(
            name='MeaningValence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meaning', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valences', to='lexicon.Meaning')),
            ],
        ),
        migrations.CreateModel(
            name='ValenceFrame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='meaningvalence',
            name='valenceFrame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='lexicon.ValenceFrame'),
        ),
        migrations.AddField(
            model_name='example',
            name='meaningValence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='lexicon.MeaningValence'),
        ),
    ]