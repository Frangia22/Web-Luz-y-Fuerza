# Generated by Django 3.2.4 on 2021-07-08 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnos', '0008_auto_20210707_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='montoRecaudado',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]