from django.contrib import admin
from turnos.models import  Turno

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'tipoCancha', 'fecha', 'celular', 'montoRecaudado', 'turnoDadoPor')


