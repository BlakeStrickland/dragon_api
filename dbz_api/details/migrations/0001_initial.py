# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('damage', models.IntegerField()),
                ('ability_range', models.CharField(max_length=255)),
                ('minimum_power_to_use', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CharacterStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_name', models.CharField(max_length=20)),
                ('home_planet', models.CharField(max_length=255)),
                ('power_level', models.IntegerField()),
                ('form', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='ability',
            name='character',
            field=models.ManyToManyField(to='details.CharacterStatistics'),
        ),
    ]