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
# Creo la vista de la home
def index(request):
    return render(request, "cancha/index.html")
# Creo el login
def loginView(request):
    if request.method == "POST":
        #Almaceno los datos 
        nombre = request.POST["nombre"]
        password = request.POST["password"]
        #Comparo los datos con los que estan  en la BD
        user = authenticate(request, nombre = nombre, password = password)
        # SI es si redirijo a la home
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        # SI no devuelvo el form con un mensaje
        else:
            return render(request, "accounts/login.html", { "mensaje" : "El nombre de usuario o la clave son incorrectas."})
    return render(request, "accounts/login.html")
# Cerrar sesión
def logoutView(request):
    pass