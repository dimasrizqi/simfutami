# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0051_auto_20190409_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transisi',
            name='update_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]