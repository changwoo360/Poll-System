# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-12 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0021_auto_20181012_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipestudy',
            name='study',
        ),
        migrations.RemoveField(
            model_name='recipestudy',
            name='user',
        ),
        migrations.DeleteModel(
            name='RecipeStudy',
        ),
    ]
