# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-10 12:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0018_listtanya_no_tanya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kucing',
            name='umur_kucing',
            field=models.CharField(choices=[('1 bulan', '1 Bulan'), ('2 bulan', '2 Bulan'), ('3 bulan', '3 Bulan'), ('4 bulan', '4 Bulan'), ('5 bulan', '5 Bulan'), ('6 bulan', '6 Bulan'), ('7 bulan', '7 Bulan'), ('8 bulan', '8 Bulan'), ('9 bulan', '9 Bulan'), ('10 bulan', '10 Bulan'), ('11 bulan', '11 Bulan'), ('1 tahun', '1 Tahun'), ('2 tahun', '2 Tahun'), ('3 tahun', '3 Tahun'), ('4 tahun', '4 Tahun'), ('5 tahun', '5 Tahun'), ('6 tahun', '6 Tahun'), ('7 tahun', '7 Tahun'), ('8 tahun', '8 Tahun'), ('9 tahun', '9 Tahun'), ('10 tahun', '10 Tahun')], max_length=10),
        ),
        migrations.AlterField(
            model_name='useractivationkey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 8, 10)),
        ),
    ]