# Generated by Django 3.0.7 on 2021-02-02 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_isguida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='isguida',
        ),
    ]
