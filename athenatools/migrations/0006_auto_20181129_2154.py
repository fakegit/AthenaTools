# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-29 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athenatools', '0005_auto_20181129_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
