# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-24 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0004_jawaban'),
    ]

    operations = [
        migrations.AddField(
            model_name='infopenyakit',
            name='info_penyakit_slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='jawaban',
            name='jawab',
            field=models.CharField(max_length=10),
        ),
    ]
