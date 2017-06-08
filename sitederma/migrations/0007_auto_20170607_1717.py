# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 17:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitederma', '0006_useractivationkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listpertanyaan',
            name='gejala',
        ),
        migrations.RemoveField(
            model_name='listpertanyaan',
            name='kode_pertanyaan',
        ),
        migrations.RemoveField(
            model_name='listpertanyaan',
            name='pertanyaan',
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_1',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda sering menggaruk?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_10',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah bulu pada daerah telinga, leher, bahu, pangkal paha, dan daerah dubur kucing anda mengalami kerontokan?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_11',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah bulu kucing anda mengalami kerontokan yang berbentuk melingkar?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_12',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kulit kucing anda berkerak?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_13',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda kulit berkerak kering?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_14',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kulit pada telinga, siku, kaki, dan perut kucing anda berkerak?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_15',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kulit kucing anda berdarah?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_16',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kulit kucing anda bernanah?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_17',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kulit kucing anda kemerahan?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_18',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kulit kucing anda terlihat kering?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_19',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada kulit kucing anda terdapat luka?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_2',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda menggaruk berlebihan?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_20',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada kulit kucing anda terdapat luka dan lecet di belakang kepala, telinga atau leher?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_21',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah warna kulit kucing anda menjadi kehitaman?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_22',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada kucing anda terlihat kutu berwarna merah kecoklatan berjalan cepat di tubuh?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_23',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada kucing anda terlihat kotoran hitam seperti pasir di punggung?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_24',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada kucing anda terlihat seperti ada butiran di bulu?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_25',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda sering menjilat?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_26',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda kadang-kadang menjilat kaki dan area tubuh lainnya?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_3',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda menggaruk daerah telinga, leher, dan kepala?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_4',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah kucing anda sering menggeleng-gelengkan kepala?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_5',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada telinga kucing anda terdapat kotoran berwarna coklat kehitaman?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_6',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah pada telinga kucing anda terdapat kotoran telinga kering (berpasir) dan tidak berminyak?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_7',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah bulu kucing anda terlihat kusam?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_8',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah bulu kucing anda mengalami kerontokan?'),
        ),
        migrations.AddField(
            model_name='listpertanyaan',
            name='indication_9',
            field=models.CharField(choices=[('1', 'Ya'), ('0.5', 'Mungkin'), ('0', 'Tidak')], max_length=100, null=True, verbose_name='Apakah bulu pada telinga kucing anda mengalami kerontokan?'),
        ),
        migrations.AlterField(
            model_name='useractivationkey',
            name='key_expires',
            field=models.DateTimeField(default=datetime.date(2017, 6, 7)),
        ),
    ]