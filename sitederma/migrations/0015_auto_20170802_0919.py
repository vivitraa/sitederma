# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-02 09:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0014_auto_20170730_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='konsultasi',
            old_name='bobotcf',
            new_name='cfp',
        ),
        migrations.AlterField(
            model_name='useractivationkey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 8, 2)),
        ),
    ]