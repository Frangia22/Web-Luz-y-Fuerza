from turnos.models import Turno
from datetime import datetime
from django import forms
from django.forms.widgets import *

class turnoForm(forms.ModelForm):
    
    class Meta:
        model = Turno
        fields = ('__all__')
        widgets = {
          'turnoDadoPor': forms.Select(),
          'fechaInicio': forms.DateTimeInput(),
          'fechaFin': forms.DateTimeInput()
    }
