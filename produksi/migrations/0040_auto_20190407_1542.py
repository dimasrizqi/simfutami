# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0039_auto_20190407_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productperpalet',
            name='tanggal_produksi',
            field=models.DateTimeField(),
        ),
    ]
