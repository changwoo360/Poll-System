# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-07 06:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0003_auto_20181007_1435'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='account',
            table='Account',
        ),
        migrations.AlterModelTable(
            name='user',
            table='User',
        ),
    ]
