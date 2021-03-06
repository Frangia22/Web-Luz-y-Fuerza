from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('calendario', views.calendarioDetail, name='calendario'),
    path('contacto', views.contacto, name='contacto'),
]