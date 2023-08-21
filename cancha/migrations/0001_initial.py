# Generated by Django 4.2.4 on 2023-08-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gasto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concepto', models.CharField(max_length=100)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateTimeField(verbose_name='Fecha y hora')),
                ('referencia', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
    ]
