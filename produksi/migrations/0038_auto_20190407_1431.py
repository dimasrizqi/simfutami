# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0037_transisi_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='pengguna',
        ),
        migrations.RemoveField(
            model_name='transisi',
            name='user',
        ),
        migrations.AddField(
            model_name='transisi',
            name='pengguna',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='produksi.pengguna'),
            preserve_default=False,
        ),
    ]
