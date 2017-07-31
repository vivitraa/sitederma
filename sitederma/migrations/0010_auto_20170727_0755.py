# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-27 07:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0009_auto_20170718_0658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jawaban',
            name='pertanyaan',
        ),
        migrations.AddField(
            model_name='listtanya',
            name='kode_gejala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tanya_gejala', to='sitederma.ListGejala'),
        ),
        migrations.AlterField(
            model_name='useractivationkey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 7, 27)),
        ),
    ]
