from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, date
from turnos.list import cancha, asistencia

# Create your models here.
class Turno(models.Model):
    #Campos a ingresar de los usuarios
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    tipoCancha = models.CharField(max_length=60, choices= cancha)
    fecha = models.DateTimeField(verbose_name='Fecha y hora')
    celular = models.CharField("Celular", max_length = 11, unique = True)
    asistio = models.CharField(max_length=9, choices= asistencia, default='Si')
    montoRecaudado = models.IntegerField(default=0)
    turnoDadoPor = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="TurnoDadoPor")

class Meta:
    verbose_name = 'Turno'
    ordering = ['fecha']
def __str__(self):
    return f'{self.nombre} {self.apellido} {self.fecha}'

