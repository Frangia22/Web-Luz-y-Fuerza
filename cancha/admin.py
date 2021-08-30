from django.contrib import admin
from cancha.models import  Gasto

@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    
    list_display = ('concepto', 'monto', 'fecha', 'referencia')

