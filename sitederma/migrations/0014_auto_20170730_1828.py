# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-30 18:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitederma', '0013_remove_infopenyakit_info_penyakit_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='kucing',
            name='pemilik',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listtanya',
            name='daftar_tanya',
            field=models.CharField(max_length=150),
        ),
    ]