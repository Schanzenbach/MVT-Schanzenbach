# Generated by Django 4.1 on 2022-08-23 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familiar',
            name='fecha_nacimiento',
        ),
    ]
