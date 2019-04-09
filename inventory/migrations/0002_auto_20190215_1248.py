# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-15 05:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cctv',
            fields=[
                ('cctv_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_cctv', models.CharField(max_length=100)),
                ('tipe_cctv', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('lokasi_cctv', models.CharField(max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
                ('catatan', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='keyboard',
            fields=[
                ('keyboard_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_keyboard', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('interface', models.CharField(choices=[('PS2', 'PS2'), ('USB', 'USB'), ('WIRELESS', 'WIRELESS'), ('SERIAL', 'SERIAL')], default='USB', max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='monitor',
            fields=[
                ('monitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_monitor', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('tipe_monitor', models.CharField(choices=[('Tabung', 'Tabung'), ('LCD', 'LCD'), ('LED', 'LED')], default='LCD', max_length=100)),
                ('ukuran_monitor', models.CharField(choices=[('14 Inch', '14 Inch'), ('15 Inch', '15 Inch'), ('16 Inch', '16 Inch'), ('17 Inch', '17 Inch'), ('18 Inch', '18 Inch'), ('19 Inch', '19 Inch')], default='14 Inch', max_length=100)),
                ('input_monitor', models.CharField(choices=[('VGA', 'VGA'), ('HDMI', 'HDMI')], default='VGA', max_length=100)),
                ('tipe_power', models.CharField(choices=[('AC', 'AC'), ('Adaptor', 'Adaptor')], default='AC', max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='motherboard',
            fields=[
                ('motherboard_id', models.AutoField(primary_key=True, serialize=False)),
                ('tipe_socket', models.CharField(max_length=100)),
                ('merek_motherboard', models.CharField(max_length=100)),
                ('tipe_motherboard', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
                ('catatan', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mouse',
            fields=[
                ('mouse_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_mouse', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='pesawat_telephone',
            fields=[
                ('pesawat_telephone_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_pesawat_telephone', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('no_extention', models.CharField(max_length=100)),
                ('lokasi_pesawat_telephone', models.CharField(max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='printer',
            fields=[
                ('printer_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_printer', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('interface', models.CharField(choices=[('PS2', 'PS2'), ('USB', 'USB'), ('WIRELESS', 'WIRELESS'), ('SERIAL', 'SERIAL')], default='USB', max_length=100)),
                ('tipe_printer', models.CharField(choices=[('Deskjet', 'Deskjet'), ('Inkjet', 'Inkjet'), ('Laser', 'Laser'), ('Monokrom', 'Monokrom')], default='Inkjet', max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='processor',
            fields=[
                ('processor_id', models.AutoField(primary_key=True, serialize=False)),
                ('merek_processor', models.CharField(choices=[('AMD', 'AMD'), ('INTEL', 'INTEL')], default='INTEL', max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('kondisi', models.CharField(choices=[('OK', 'OK'), ('RUSAK', 'RUSAK')], default='OK', max_length=100)),
                ('catatan', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='komputer',
            name='tipe_komputer',
            field=models.CharField(choices=[('PC', 'PC'), ('NComputing', 'NComputing')], default='PC', max_length=100),
        ),
        migrations.AddField(
            model_name='memory',
            name='serial_number',
            field=models.CharField(default='please update', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='psu',
            name='serial_number',
            field=models.CharField(default='please update', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storage',
            name='serial_number',
            field=models.CharField(default='please update', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='processor',
            name='dipakai_pada_komputer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.komputer'),
        ),
        migrations.AddField(
            model_name='printer',
            name='dipakai_pada_komputer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.komputer'),
        ),
        migrations.AddField(
            model_name='mouse',
            name='dipakai_pada_komputer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.komputer'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='dipakai_pada_komputer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.komputer'),
        ),
        migrations.AddField(
            model_name='monitor',
            name='dipakai_pada_komputer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.komputer'),
        ),
        migrations.AddField(
            model_name='keyboard',
            name='dipakai_pada_komputer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.komputer'),
        ),
    ]
