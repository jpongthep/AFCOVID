# Generated by Django 3.2.5 on 2021-07-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0004_auto_20210721_1116'),
    ]

    operations = [
        migrations.CreateModel(
            name='AMEDPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PersonID', models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='เลขบัตรประชาชน')),
                ('HNNumber', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='เลขผู้ป่วยนอก')),
                ('ANNumber', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='เลขผู้ป่วยใน')),
                ('Fullname', models.CharField(blank=True, default='-', max_length=255, null=True, verbose_name='ชื่อผู้ป่วย')),
                ('Mobile', models.CharField(blank=True, max_length=20, null=True, verbose_name='เบอร์มือถือ')),
                ('Symtom', models.IntegerField(choices=[(0, 'ไม่ระบุ'), (1, 'ผู้ป่วยสีเขียว'), (2, 'ผู้ป่วยสีเหลืองอ่อน'), (3, 'ผู้ป่วยสีเหลืองเข้ม'), (4, 'ผู้ป่วยสีแดง'), (5, 'หายป่วย'), (6, 'เสียชีวิต'), (7, 'ผู้ใกล้ชิดเสี่ยงสูง'), (8, 'ผู้ใกล้ชิดปลอดเชื้อ'), (9, 'ผู้ใกล้ชิดติดเชื้อ')], default=0, null=True)),
            ],
            options={
                'verbose_name_plural': ' [AMEDPatient]',
            },
        ),
    ]
