from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('calendario', views.calendarioDetail, name='calendario'),
    path('contacto', views.contacto, name='contacto'),
    path('ganancias', views.ganancias.as_view(), name='ganancias'),
    path('nuevoGasto', views.nuevoGasto.as_view(), name='nuevoGasto'),
    path('detalleGasto', views.detalleGasto.as_view(), name='detalleGasto'),
    path('eliminar/<int:pk>', views.eliminarGasto.as_view() , name='eliminarGasto'),
]