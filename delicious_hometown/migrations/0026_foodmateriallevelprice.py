# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-12 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0025_choicemarket_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMaterialLevelPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('food_material_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.FoodMaterialLevel')),
            ],
            options={
                'db_table': 'FoodMaterialLevelPrice',
            },
        ),
    ]