# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-03 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=80, verbose_name='密码'),
            preserve_default=False,
        ),
    ]
