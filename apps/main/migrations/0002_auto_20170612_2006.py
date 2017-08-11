# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорие', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='main'),
        ),
        migrations.AlterField(
            model_name='item',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]