from django.contrib import admin
from turnos.models import  Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'apellido', 'tipoCancha', 'fecha', 'celular', 'montoRecaudado', 'turnoDadoPor')


