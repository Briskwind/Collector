# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-15 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20181115_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=256, verbose_name='作者'),
            preserve_default=False,
        ),
    ]
