# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0019_auto_20190327_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kode_product',
            field=models.CharField(default='1', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productperpalet',
            name='nomor_batch',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
    ]
