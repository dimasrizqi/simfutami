# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-27 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0018_auto_20190327_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='productperpalet',
            name='status',
        ),
    ]
