# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-13 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0021_auto_20170813_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='kucing',
            name='kode_kucing',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
