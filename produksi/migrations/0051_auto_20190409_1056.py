# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 10:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0050_auto_20190409_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transisi',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 10, 56, 0, 252796)),
        ),
    ]
