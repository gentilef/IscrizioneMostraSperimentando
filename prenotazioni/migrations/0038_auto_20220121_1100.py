# Generated by Django 3.0.7 on 2022-01-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0037_auto_20220120_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentiprenotazione',
            name='orario_turno',
        ),
        migrations.RemoveField(
            model_name='movimentiprenotazione',
            name='settore',
        ),
    ]
