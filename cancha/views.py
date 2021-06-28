from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from turnos.models import Turno
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def index(request):
    return render(request, "cancha/index.html")