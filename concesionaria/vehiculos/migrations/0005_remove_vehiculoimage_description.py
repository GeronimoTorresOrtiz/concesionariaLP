# Generated by Django 5.0.7 on 2024-08-08 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0004_vehiculoimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculoimage',
            name='description',
        ),
    ]
