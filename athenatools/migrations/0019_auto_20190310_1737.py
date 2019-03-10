# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athenatools', '0018_auto_20190310_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='check_freeze',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\x86\xbb\xe5\x93\x81\xe6\xb8\xa9\xe5\xba\xa6\xe2\x89\xa4-12\xe2\x84\x83\xe4\xb8\x94\xe6\x97\xa0\xe8\xbd\xaf\xe5\x8c\x96'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='check_label',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe\xe6\xad\xa3\xe5\xb8\xb8'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='check_odorless',
            field=models.BooleanField(default=True, verbose_name=b'\xe6\x97\xa0\xe5\xbc\x82\xe5\x91\xb3'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='check_package',
            field=models.BooleanField(default=True, verbose_name=b'\xe5\x8c\x85\xe8\xa3\x85\xe5\xae\x8c\xe5\xa5\xbd'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='storage',
            field=models.CharField(choices=[('\u5ba4\u6e29', '\u5ba4\u6e29'), ('\u51b7\u51bb', '\u51b7\u51bb'), ('\u51b7\u85cf', '\u51b7\u85cf')], default='\u5ba4\u6e29', max_length=255, verbose_name=b'\xe9\xbb\x98\xe8\xae\xa4\xe8\xb4\xae\xe8\x97\x8f\xe6\x96\xb9\xe5\xbc\x8f'),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_check_freeze',
            field=models.BooleanField(default=True, verbose_name=b'\xe9\xbb\x98\xe8\xae\xa4\xe5\x86\xbb\xe5\x93\x81\xe6\xb8\xa9\xe5\xba\xa6\xe2\x89\xa4-12\xe2\x84\x83\xe4\xb8\x94\xe6\x97\xa0\xe8\xbd\xaf\xe5\x8c\x96'),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_check_label',
            field=models.BooleanField(default=True, verbose_name=b'\xe9\xbb\x98\xe8\xae\xa4\xe6\xa0\x87\xe7\xad\xbe\xe6\xad\xa3\xe5\xb8\xb8'),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_check_odorless',
            field=models.BooleanField(default=True, verbose_name=b'\xe9\xbb\x98\xe8\xae\xa4\xe6\x97\xa0\xe5\xbc\x82\xe5\x91\xb3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='default_check_package',
            field=models.BooleanField(default=True, verbose_name=b'\xe9\xbb\x98\xe8\xae\xa4\xe5\x8c\x85\xe8\xa3\x85\xe5\xae\x8c\xe5\xa5\xbd'),
        ),
    ]
