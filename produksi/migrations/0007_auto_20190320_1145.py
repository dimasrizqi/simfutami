# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0006_gudangracking_productkeluar_tujuan'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='productkeluar',
        #     name='id',
        # ),
        # migrations.RemoveField(
        #     model_name='tujuan',
        #     name='nomor_do',
        # ),
        # migrations.RemoveField(
        #     model_name='tujuan',
        #     name='nomor_segel',
        # ),
        # migrations.RemoveField(
        #     model_name='tujuan',
        #     name='referensi_qc',
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='list_product',
        #     field=models.CharField(default='', max_length=500),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='nomor_do',
        #     field=models.CharField(default='', max_length=20),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='nomor_segel',
        #     field=models.CharField(default='', max_length=20),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='productkeluar_id',
        #     field=models.AutoField(default='', primary_key=True, serialize=False),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='referensi_qc',
        #     field=models.CharField(choices=[('OK', 'OK'), ('NOT OK', 'NOT OK')], default='', max_length=10),
        #     preserve_default=False,
        # ),
        # migrations.AddField(
        #     model_name='productkeluar',
        #     name='tujuan',
        #     field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='produksi.tujuan'),
        #     preserve_default=False,
        # ),
    ]
