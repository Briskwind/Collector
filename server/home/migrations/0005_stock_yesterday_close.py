# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-01-13 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190113_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='yesterday_close',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='昨日收盘'),
        ),
    ]
