# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-15 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_book_booktag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='Introduction',
            new_name='introduction',
        ),
    ]
