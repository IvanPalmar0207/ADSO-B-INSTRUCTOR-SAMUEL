from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from habitacionesGestion.serializer import tb_tipoHabitacionSerializer,tb_mobiliarioSerializer,tb_estadoSerializer, tb_habitacionSerializer
from habitacionesGestion.models import tb_tipoHabitacion, tb_mobiliario, tb_estado, tb_habitacion
from rest_framework import viewsets

# Create your views here.

class tipoHabitacionViewSet(viewsets.ModelViewSet):
    queryset = tb_tipoHabitacion.objects.all()
    serializer_class = tb_tipoHabitacionSerializer
    
class mobiliarioViewSet(viewsets.ModelViewSet):
    queryset = tb_mobiliario.objects.all()
    serializer_class = tb_mobiliarioSerializer
    
class estadoViewSet(viewsets.ModelViewSet):
    queryset = tb_estado.objects.all()
    serializer_class = tb_estadoSerializer

class habitacionViewSet(viewsets.ModelViewSet):
    queryset = tb_habitacion.objects.all()
    serializer_class = tb_habitacionSerializer

@api_view(['GET'])
def gestionApisHabitaciones(request):    
    apiUrl = {
        "Api del tipo de habitacion" : "/tipoHabitacion/",
        "Api del estado de la habitacion" : "/estadoHabitacion/",
        "Api del mobiliario de la habitacion" : "/mobiliario/",
        "Api de la Habitacion" : "/habitacion/"    
    }
    return Response(apiUrl)