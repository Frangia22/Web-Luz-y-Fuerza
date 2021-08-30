from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Gastos
class Gasto(models.Model):
    #Campos para ingresar gastos
    concepto = models.CharField(max_length=100)
    monto = models.IntegerField()
    fecha = models.DateTimeField(verbose_name='Fecha y hora')
    referencia = models.CharField(max_length=100, default='', null=True, blank=True)