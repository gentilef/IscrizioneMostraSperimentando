# Generated by Django 3.0.7 on 2021-02-07 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prenotazioni', '0033_auto_20210207_0938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prenotazione',
            old_name='ora',
            new_name='ora_prenotazione',
        ),
    ]
