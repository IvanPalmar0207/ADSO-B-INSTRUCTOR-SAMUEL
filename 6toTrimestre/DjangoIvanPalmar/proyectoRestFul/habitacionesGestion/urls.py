from django.urls import path
from habitacionesGestion.views import gestionHabitaciones,gestionTiposHabitacion, tipoHabitacionTodos, tipoHabitacionUno,tipoHabitacionAgregar

urlpatterns = [
    path('gestionHabitaciones', gestionHabitaciones, name = 'gestionHabitaciones'),
    path('gestionTiposHabitacion/',gestionTiposHabitacion,name='gestionTiposHabitacion'),
    path('tipoHabitacionTodos/',tipoHabitacionTodos, name = 'tipoHabitacionTodos'),
    path('tipoHabitacionUno/<id>',tipoHabitacionUno, name = 'tipoHabitacionUno'),
    path('tipoHabitacionAgregar/',tipoHabitacionAgregar, name = 'tipoHabitacionAgregar')
]
