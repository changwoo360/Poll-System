# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-10 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delicious_hometown', '0016_auto_20181010_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='菜谱名称')),
                ('introduce', models.CharField(max_length=1024, null=True, verbose_name='详细做法')),
            ],
            options={
                'db_table': 'RecipeName',
            },
        ),
        migrations.RemoveField(
            model_name='recipelevel',
            name='recipe_class',
        ),
        migrations.RemoveField(
            model_name='restaurantrecipe',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='restaurantrecipe',
            name='User',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeclass',
            name='name',
            field=models.CharField(max_length=16, verbose_name='菜系名称'),
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
        migrations.AddField(
            model_name='recipename',
            name='recipe_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.RecipeClass', verbose_name='菜系'),
        ),
        migrations.AddField(
            model_name='recipelevel',
            name='recipe_name',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='delicious_hometown.RecipeName'),
            preserve_default=False,
        ),
    ]
