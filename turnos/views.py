from django.shortcuts import render
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
    success_url = reverse_lazy('index')
