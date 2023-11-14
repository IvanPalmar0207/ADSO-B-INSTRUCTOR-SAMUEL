from django.urls import path
from reservaGestion.views import reserva, insertarReserva, mostrarReserva,eliminarReserva, actualizaReserva, actualizarReserva

urlpatterns = [
    path('reserva',reserva,name='reserva'),
    path('insertarReserva/',insertarReserva,name='insertarReserva'),
    path('mostrarReserva',mostrarReserva,name='mostrarReserva'),
    path('eliminarReserva/<codigo>',eliminarReserva,name='eliminarReserva'),
    path('actualizaReserva/<codigo>',actualizaReserva,name='actualizaReserva'),
    path('actualizaReserva/actualizarReserva/',actualizarReserva,name='actualizarReserva')
]
