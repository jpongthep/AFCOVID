# Generated by Django 3.2.5 on 2021-07-19 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0012_auto_20210718_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ConfirmedPatient',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='แพทย์ยืนยันข้อมูล'),
        ),
    ]
