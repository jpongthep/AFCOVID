# Generated by Django 3.2.5 on 2021-08-23 23:06

import ATKQueue.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reserve', models.DateField(default=ATKQueue.models.tomorrow, verbose_name='วันจอง')),
                ('slot', models.CharField(blank=True, choices=[('--', '-------'), ('08', '0800 - 0900'), ('09', '0900 - 1000'), ('10', '1000 - 1100'), ('11', '1100 - 1200'), ('13', '1300 - 1400')], default='--', max_length=2, null=True, verbose_name='ช่วงเวลา')),
                ('queue_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='เลขที่คิว')),
                ('person_id', models.CharField(blank=True, max_length=13, null=True, verbose_name='เลขบัตรประชาชน')),
                ('is_present', models.BooleanField(blank=True, default=True, null=True, verbose_name='เข้าตรวจ')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'ตารางจองคิว [Queue]',
            },
        ),
        migrations.CreateModel(
            name='DateTimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_reserve', models.DateField(default=ATKQueue.models.tomorrow, verbose_name='วันจอง')),
                ('slot', models.CharField(blank=True, choices=[('--', '-------'), ('08', '0800 - 0900'), ('09', '0900 - 1000'), ('10', '1000 - 1100'), ('11', '1100 - 1200'), ('13', '1300 - 1400')], default='--', max_length=2, null=True, verbose_name='ช่วงเวลา')),
                ('number_queue', models.IntegerField(blank=True, default=200, null=True, verbose_name='จำนวนคิว')),
                ('reserve_queue', models.IntegerField(blank=True, default=1, null=True, verbose_name='จองแล้ว')),
                ('update_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updater', to=settings.AUTH_USER_MODEL, verbose_name='ผู้แก้ไขข้อมูล ')),
            ],
            options={
                'verbose_name_plural': 'ตารางวันเวลา [DateTimeSlot]',
            },
        ),
    ]