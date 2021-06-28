url cancha
'''
    #path('login', views.login_view, name='login'),
    #path('logout', views.logout_view, name='logout'),
    #path('calendario', views.calendarioDetail, name='calendario'),
    '''
url turnos
"""
    path('turno/nuevo', views.nuevoTurno.as_view() , name='nuevoTurno'),
    path('turno/detalle', views.detalleTurno , name='detalleTurno'),
    path('turno/editar/<int:pk>', views.editarTurno.as_view() , name='editarTurno'),
    path('turno/eliminar/<int:pk>', views.eliminarTurno.as_view() , name='eliminarTurno'),
    """