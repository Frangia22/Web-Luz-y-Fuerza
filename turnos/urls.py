from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('nuevo', views.nuevoTurno.as_view() , name='nuevoTurno')
]