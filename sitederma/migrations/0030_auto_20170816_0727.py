# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-16 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0029_auto_20170816_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riwayat',
            name='hasil_diagnosa',
            field=models.FloatField(max_length=30, null=True),
        ),
    ]