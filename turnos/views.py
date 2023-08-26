from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime, date
from turnos.models import Turno
from turnos.forms import turnoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from django.urls import reverse, reverse_lazy

# Create your views here.
class nuevoTurno(LoginRequiredMixin, CreateView):
    model = Turno
    form_class = turnoForm
    template_name = "turnos/nuevoTurno.html"
    success_url = reverse_lazy('detalleTurno')
class detalleTurno(LoginRequiredMixin, ListView):
    model = Turno
    template_name = "turnos/detalleTurno.html"
    context_object_name = 'turnos'
    paginate_by = 7
    ordering = ['-fechaInicio']

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        mes = date.today()
        contexto['montoTotal'] = Turno.objects.filter(fechaInicio__month=mes.month).aggregate(Sum('montoRecaudado')).get('montoRecaudado__sum')
        return contexto

class eliminarTurno(LoginRequiredMixin, DeleteView):
    model = Turno
    template_name = "turnos/eliminarTurno.html"
    success_url = reverse_lazy('index')

class editarTurno(LoginRequiredMixin, UpdateView):
    model = Turno
    form_class = turnoForm
    template_name = "turnos/editarTurno.html"
    success_url = reverse_lazy('detalleTurno')

