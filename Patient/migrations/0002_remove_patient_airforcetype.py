# Generated by Django 3.2.5 on 2021-07-25 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='AirforceType',
        ),
    ]