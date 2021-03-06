# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20190218_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laptop',
            name='merek_laptop',
        ),
        migrations.AlterField(
            model_name='komputer',
            name='tipe_komputer',
            field=models.CharField(choices=[('PC', 'PC'), ('NComputing', 'NComputing'), ('Laptop', 'Laptop')], default='PC', max_length=100),
        ),
        migrations.AlterField(
            model_name='storage',
            name='kapasitas',
            field=models.CharField(choices=[('40Gb', '40Gb'), ('80Gb', '80Gb'), ('120Gb', '120Gb'), ('250Gb', '250Gb'), ('320Gb', '320Gb'), ('500Gb', '500Gb'), ('1Tb', '1Tb'), ('2Tb', '2Tb')], default='320 Gb', max_length=100),
        ),
        migrations.DeleteModel(
            name='laptop',
        ),
    ]
