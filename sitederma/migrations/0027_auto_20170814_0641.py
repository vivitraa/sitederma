# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-14 06:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0026_auto_20170814_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kucing',
            name='umur_kucing',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
