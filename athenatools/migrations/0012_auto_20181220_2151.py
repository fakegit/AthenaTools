# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-20 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athenatools', '0011_auto_20181220_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='group',
            field=models.CharField(blank=True, max_length=255, verbose_name=b'\xe7\xbb\x84\xe5\x88\xab'),
        ),
    ]
