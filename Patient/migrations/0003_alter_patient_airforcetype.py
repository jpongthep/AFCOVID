# Generated by Django 3.2.5 on 2021-08-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0002_auto_20210802_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='AirforceType',
            field=models.IntegerField(blank=True, choices=[(0, 'ไม่ระบุ'), (1, 'ทหารประจำการ'), (8, 'นักเรียนทหาร'), (2, 'พลทหาร'), (3, 'พนง.ราชการ'), (4, 'ลูกจ้างประจำ'), (5, 'ลูกจ้างชั่วคราว'), (6, 'ครอบครัว ทอ.'), (7, 'บุคคลภายนอก')], default=0, null=True, verbose_name='ประเภทข้าราชการ'),
        ),
    ]
