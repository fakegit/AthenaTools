# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('athenatools', '0016_product_exp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='exp',
            new_name='default_exp',
        ),
    ]
