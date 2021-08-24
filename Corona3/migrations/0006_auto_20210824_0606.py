# Generated by Django 3.2.5 on 2021-08-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Corona3', '0005_auto_20210818_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corona3',
            name='CareerPatient',
            field=models.CharField(blank=True, default='-', max_length=30, null=True, verbose_name='อาชีพ(ระบุลักษณะงาน เช่น บุคลากรทางการแพทย์)'),
        ),
        migrations.AlterField(
            model_name='corona3',
            name='NearCovid',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='ได้ดูแลหรือสัมผัสใกล้ชิดกับผู้ป่วยอาการคล้ายไข้หวัดใหญ่หรือปอดอักเสบ'),
        ),
        migrations.AlterField(
            model_name='corona3',
            name='TypeLive_Other',
            field=models.CharField(blank=True, default='-', max_length=200, null=True, verbose_name='ระบุลักษณะการพักอาศัย'),
        ),
    ]