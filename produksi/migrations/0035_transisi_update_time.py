# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0034_status_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='transisi',
            name='update_time',
            field=models.DateTimeField(default='2019-04-07 20:44'),
            preserve_default=False,
        ),
    ]
