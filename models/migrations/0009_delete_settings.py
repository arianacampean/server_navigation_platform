# Generated by Django 4.0 on 2022-05-17 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_alter_trip_latitude_alter_trip_longitude'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
