# Generated by Django 3.2.5 on 2021-07-31 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Corona3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corona3',
            name='CheckAntibody1Neg',
            field=models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Antibody ครั้งที่ 1 Neg'),
        ),
        migrations.AlterField(
            model_name='corona3',
            name='CheckAntibody2Neg',
            field=models.CharField(blank=True, default='-', max_length=10, null=True, verbose_name='Anitibody ครั้งที่ 2 Neg'),
        ),
    ]
