# Generated by Django 3.2.4 on 2021-06-27 00:34

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('tipoCancha', models.CharField(choices=[('Padel', 'Padel'), ('Futbol', 'Futbol')], max_length=60)),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('celular', models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message="Número debe ser ingresado en formato '+549XXXXXXXXXX'.", regex='^\\+?549?\\d{10}$')], verbose_name='Celular')),
            ],
        ),
    ]
