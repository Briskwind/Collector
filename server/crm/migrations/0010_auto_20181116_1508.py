# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-16 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0009_auto_20181116_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=256, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(default='', max_length=256, verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='book',
            name='introduction',
            field=models.CharField(default='', max_length=512, verbose_name='简介'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='', max_length=128, verbose_name='书名称'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(default='', max_length=128, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.CharField(default='', max_length=256, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.CharField(default='', max_length=256, verbose_name='链接'),
        ),
    ]
