# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0008_auto_20170718_0444'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ListPertanyaan',
        ),
        migrations.AddField(
            model_name='jawaban',
            name='pertanyaan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitederma.ListTanya'),
        ),
    ]
