# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='characterstatistics',
            old_name='form',
            new_name='highest_form',
        ),
    ]