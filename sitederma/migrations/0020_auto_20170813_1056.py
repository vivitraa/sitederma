# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-13 10:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0019_auto_20170810_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivationkey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 8, 13)),
        ),
    ]
