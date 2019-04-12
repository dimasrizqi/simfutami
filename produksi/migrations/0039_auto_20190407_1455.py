# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0038_auto_20190407_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='gudangracking',
            name='pengguna',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='produksi.pengguna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='pengguna',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='produksi.pengguna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productperpalet',
            name='pengguna',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='produksi.pengguna'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status_product',
            name='pengguna',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='produksi.pengguna'),
            preserve_default=False,
        ),
    ]
