# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-12 03:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0020_recipestudy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userrecipe',
            old_name='User',
            new_name='user',
        ),
        migrations.AlterModelTable(
            name='userrecipe',
            table='UserRecipe',
        ),
    ]
