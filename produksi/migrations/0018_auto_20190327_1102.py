# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 04:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0017_auto_20190327_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transisi',
            name='product_per_palet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produksi.productperpalet'),
        ),
        migrations.AlterField(
            model_name='transisi',
            name='status_perpindahan',
            field=models.CharField(choices=[('CONVEYOR', 'CONVEYOR'), ('GUDANG TRANSISI', 'GUDANG TRANSISI'), ('GUDANG RACKING', 'GUDANG RACKING')], max_length=100),
        ),
    ]
