from django.urls import path,include
from habitacionesGestion.views import tipoHabitacionViewSet, mobiliarioViewSet, estadoViewSet, habitacionViewSet
from habitacionesGestion.views import gestionApisHabitaciones
from rest_framework import routers

routerTipoHabitacion = routers.DefaultRouter()
routerTipoHabitacion.register(r'tiposHabitacion',tipoHabitacionViewSet)

routerMobiliario = routers.DefaultRouter()
routerMobiliario.register(r'mobiliario',mobiliarioViewSet)

routerEstado = routers.DefaultRouter()
routerEstado.register(r'estadoHabitacion', estadoViewSet)

routerHabitacion = routers.DefaultRouter()
routerHabitacion.register(r'habitacion', habitacionViewSet)

urlpatterns = [
    path('', gestionApisHabitaciones, name = 'gestionApisHabitaciones'),
    path('tipoHabitacion/',include(routerTipoHabitacion.urls)),
    path('mobiliario/',include(routerMobiliario.urls)),
    path('estadoHabitacion/', include(routerEstado.urls)),
    path('habitacion/', include(routerHabitacion.urls))
]