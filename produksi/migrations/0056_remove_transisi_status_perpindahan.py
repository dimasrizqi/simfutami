# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-11 03:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0055_auto_20190409_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transisi',
            name='status_perpindahan',
        ),
    ]
