from django.urls import path
from habitacionesGestion.views import inicioHabitaciones, volver, ingresarTipoHabitacion, verTipoHabitacion,eliminarTipoHabitacion, actualizaTipoHabitacion, actualizarTipoHabitacion, mobiliario, insertarMobiliario, mostrarMobiliario, eliminarMobiliario, actualizaMobiliario, actualizarMobiliario, habitaciones, insertarHabitaciones, mostrarHabitaciones,eliminarHabitaciones, actualizaHabitaciones, actualizarHabitaciones

urlpatterns = [
    path('inicioHabitaciones',inicioHabitaciones, name='inicioHabitaciones'),
    path('volver',volver,name='volver'),
    path('ingresarTipoHabitacion/',ingresarTipoHabitacion,name='ingresarTipoHabitacion'),
    path('verTipoHabitacion',verTipoHabitacion,name='verTipoHabitacion'),
    path('eliminarTipoHabitacion/<codigo>',eliminarTipoHabitacion, name='eliminarTipoHabitacion'),
    path('actualizaTipoHabitacion/<codigo>',actualizaTipoHabitacion, name='actualizaTipoHabitacion'),
    path('actualizaTipoHabitacion/actualizarTipoHabitacion/',actualizarTipoHabitacion,name='actualizarTipoHabitacion'),
    path('mobiliario',mobiliario, name='mobiliario'),
    path('insertarMobiliario/',insertarMobiliario,name='insertarMobiliario'),
    path('mostrarMobiliario',mostrarMobiliario,name='mostrarMobiliario'),
    path('eliminarMobiliario/<codigo>',eliminarMobiliario,name='eliminarMobiliario'),
    path('actualizaMobiliario/<codigo>',actualizaMobiliario, name='actualizaMobiliario'),
    path('actualizaMobiliario/actualizarMobiliario/',actualizarMobiliario,name ='actualizarMobiliario'),
    path('habitaciones',habitaciones,name='habitaciones'),
    path('insertarHabitaciones/',insertarHabitaciones,name='insertarHabitaciones'),
    path('mostrarHabitaciones',mostrarHabitaciones,name='mostrarHabitaciones'),
    path('eliminarHabitaciones/<codigo>',eliminarHabitaciones,name='eliminarHabitaciones'),
    path('actualizaHabitaciones/<codigo>',actualizaHabitaciones,name='actualizaHabitaciones'),
    path('actualizaHabitaciones/actualizarHabitaciones/',actualizarHabitaciones,name='actualizarHabitaciones')
]