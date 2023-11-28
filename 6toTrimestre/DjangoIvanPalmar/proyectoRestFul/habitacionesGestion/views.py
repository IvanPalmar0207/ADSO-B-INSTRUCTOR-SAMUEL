from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from habitacionesGestion.serializer import tb_tipoHabitacionSerializer,tb_mobiliarioSerializer,tb_estadoSerializer, tb_habitacionSerializer
from habitacionesGestion.models import tb_tipoHabitacion, tb_mobiliario, tb_estado, tb_habitacion

# Create your views here.

def gestionHabitaciones(request):
    return render(request,'gestionHabitaciones.html')

#CRUD del tipo de Habitacion

@api_view(['GET'])
def gestionTiposHabitacion(request):    
    apiUrl = {
        "Todos los tipos de habitacion" : "/tipoHabitacionTodos/",
        "Un solo tipo de habitacion" : "/tipoHabitacionUno/<id>",
        "Crear un tipo de habitacion" : "/tipoHabitacionAgregar/",
        "Actualizar un tipo de habitacion" : "/tipoHabitacionActualizar/<id>",
        "Elimnar un tipo de habitacion" : "/tipoHabitacionEliminar/<id>"
    }
    return Response(apiUrl)

@api_view(['GET'])
def tipoHabitacionTodos(request):
    try:
        tipoHabitacion = tb_tipoHabitacion.objects.all()
        serializador = tb_tipoHabitacionSerializer(tipoHabitacion, many = True)
    except Exception:
        return redirect(gestionTiposHabitacion)
    else:
        return Response(serializador.data)
    
@api_view(['GET'])
def tipoHabitacionUno(request,id):
    try:
        tipoHabitacion = tb_tipoHabitacion.objects.get(codigo_tpH=id)
        serializador = tb_tipoHabitacionSerializer(tipoHabitacion, many = False)
    except Exception:
        return redirect(gestionTiposHabitacion)
    else:
        return Response(serializador.data)
    
@api_view(['POST'])
def tipoHabitacionAgregar(request):
    serializador = tb_tipoHabitacionSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(serializador.data)
    else:
        return redirect(gestionTiposHabitacion)
    
#CRUD del mobiliario


#CRUD del estado


#CRUD de la Habitacion