# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0027_auto_20190404_1111'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='status',
            new_name='status_product',
        ),
    ]
