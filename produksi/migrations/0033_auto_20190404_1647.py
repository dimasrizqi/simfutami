# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produksi', '0032_status_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status_product',
            name='product_per_palet',
        ),
        migrations.RemoveField(
            model_name='status_product',
            name='status_product',
        ),
        migrations.DeleteModel(
            name='status_product',
        ),
    ]
