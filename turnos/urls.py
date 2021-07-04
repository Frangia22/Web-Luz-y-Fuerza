from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('nuevo', views.nuevoTurno.as_view() , name='nuevoTurno'),
    path('detalle', views.detalleTurno.as_view() , name='detalleTurno'),
    path('eliminar/<int:pk>', views.eliminarTurno.as_view() , name='eliminarTurno'),
    path('editar/<int:pk>', views.editarTurno.as_view() , name='editarTurno')
]