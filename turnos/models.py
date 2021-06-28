from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import datetime, date
from django.core.validators import RegexValidator
from turnos.list import cancha

# Create your models here.
class Turno(models.Model):
    #Campos a ingresar de los usuarios
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    tipoCancha = models.CharField(max_length=60, choices= cancha)
    fecha = models.DateTimeField(verbose_name='Fecha', default=datetime.now)
    celular_regex = RegexValidator(regex=r'^\+?54?\d{10}$', message = "Número debe ser ingresado en formato '+54XXXXXXXXXX'.")
    celular = models.CharField("Celular", validators=[celular_regex], max_length = 14, unique = True)

class Meta:
    verbose_name = 'Turno'
    ordering = ['fecha']
def __str__(self):
    return f'{self.nombre} {self.apellido} {self.fecha}'

