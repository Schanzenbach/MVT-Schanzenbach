# Generated by Django 4.1 on 2022-08-23 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppDesafio', '0002_remove_familiar_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='fecha_nacimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
