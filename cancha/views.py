from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from turnos.models import Turno
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
import datetime

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
#Contacto 
def contacto(request):
    return render(request, "cancha/contacto.html")
#Calendario
    # Muestra el calendario con las distintas reservas    
def calendarioDetail(request):
    all_events = Turno.objects.all()
    get_event_types = Turno.objects.only('event_type')

    # if filters applied then get parameter and filter based on condition else return object
    if request.GET:  
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = Turno.objects.all()
        else:   
            all_events = Turno.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.nombre, i.fecha
            start_date = datetime.datetime.strptime(str(i.fecha.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
            event_sub_arr['start'] = start_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events":all_events,
        "get_event_types":get_event_types,

    }
    return render(request,'cancha/calendario.html',context)
