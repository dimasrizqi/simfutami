# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-09 06:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0053_auto_20190409_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status_product',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 9, 6, 15, 47, 761736, tzinfo=utc)),
        ),
    ]
