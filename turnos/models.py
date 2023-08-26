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
    tipoCancha = models.CharField(max_length=60, choices= cancha)
    fechaInicio = models.DateTimeField(verbose_name='Fecha y hora inicio')
    fechaFin = models.DateTimeField(verbose_name='Fecha y hora fin')    
    celular = models.CharField("Celular", max_length = 11, null=True, default='', blank=True)
    afiliado = models.IntegerField(null=True, default='0', blank=True)
    asistio = models.CharField(max_length=9, choices= asistencia, default='Si')
    montoRecaudado = models.IntegerField(default='', null=True, blank=True)
    observaciones = models.TextField(null= True, default='No se registraron datos', blank=True)
    turnoDadoPor = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="TurnoDadoPor")

class Meta:
    verbose_name = 'Turno'
    ordering = ['fechaInicio']
def __str__(self):
    return f'{self.nombre} {self.apellido} {self.fechaInicio}'

