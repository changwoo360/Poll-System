# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-07 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0008_auto_20181007_1550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambry',
            old_name='food_material_id',
            new_name='food_material',
        ),
        migrations.RenameField(
            model_name='ambry',
            old_name='user_id',
            new_name='user',
        ),
    ]
