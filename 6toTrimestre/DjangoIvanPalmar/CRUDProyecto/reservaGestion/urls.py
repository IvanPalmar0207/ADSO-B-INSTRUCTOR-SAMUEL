from django.urls import path
from reservaGestion.views import reserva, insertarReserva, mostrarReserva,eliminarReserva, actualizaReserva, actualizarReserva
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('reserva',reserva,name='reserva'),
    path('insertarReserva/',csrf_exempt(insertarReserva),name='insertarReserva'),
    path('mostrarReserva',mostrarReserva,name='mostrarReserva'),
    path('eliminarReserva/<codigo>',csrf_exempt(eliminarReserva),name='eliminarReserva'),
    path('actualizaReserva/<codigo>',actualizaReserva,name='actualizaReserva'),
    path('actualizaReserva/actualizarReserva/',csrf_exempt(actualizarReserva),name='actualizarReserva')
]