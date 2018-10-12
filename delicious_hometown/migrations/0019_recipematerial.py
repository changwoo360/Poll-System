# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-10 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0018_auto_20181010_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.RecipeLevel')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.FoodMaterial')),
            ],
            options={
                'db_table': 'RecipeMaterial',
            },
        ),
    ]
