# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0040_auto_20190407_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='productperpalet',
            name='update_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]