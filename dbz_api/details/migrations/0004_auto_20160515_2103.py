# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0003_characterstatistics_special_abilities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ability',
            old_name='name',
            new_name='ability_name',
        ),
    ]