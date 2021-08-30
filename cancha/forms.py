from cancha.models import Gasto
from datetime import datetime
from django import forms
from django.forms.widgets import *

class gastoForm(forms.ModelForm):
    
    class Meta:
        model = Gasto
        fields = ('__all__')
        widgets = {
          'fecha': forms.DateTimeInput()
    }