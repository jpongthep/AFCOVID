# Generated by Django 3.2.5 on 2021-07-17 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Patient', '0008_auto_20210717_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='Treatment',
            new_name='CurrentTreatment',
        ),
    ]
