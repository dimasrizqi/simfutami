# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 14:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0036_remove_transisi_update_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='transisi',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='produksi.user'),
            preserve_default=False,
        ),
    ]
