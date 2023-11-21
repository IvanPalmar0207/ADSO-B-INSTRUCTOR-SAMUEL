from django.shortcuts import render,redirect
from reservaGestion.models import tb_reserva
from habitacionesGestion.models import tb_habitacion
from usuariosGestion.models import tb_usuarios
# Create your views here.

def reserva(request):
    habitacion = tb_habitacion.objects.all()
    contexto = {
        'habitaciones' : habitacion
    }
    return render(request,'reserva.html',contexto)

def insertarReserva(request):
    try:
        codigoRes1 = request.POST['codigoRes']
        numeroDoc = tb_usuarios.objects.get(numeroDocumento_cli = request.POST['numeroDoc'])
        fechaLlegada = request.POST['fechaLlegada']
        fechaSalida = request.POST['fechaSalida']
        cantidadJovenes = request.POST['cantidadJovenes']
        cantidadAdultos = request.POST['cantidadAdultos']
        tipoHabitacion = tb_habitacion.objects.get(codigo_hab = request.POST['tipoHabitacion'])

        if fechaLlegada<fechaSalida:        
            reserva = tb_reserva.objects.create(codigo_res = codigoRes1, numeroDocumento_cli = numeroDoc, fechaInicio_res = fechaLlegada, fechaSalida_res = fechaSalida, cantidadJovenes_res =cantidadJovenes, cantidadAdultos_res = cantidadAdultos, codigo_hab = tipoHabitacion)
        else:
            return render(request, 'errorReserva.html')

    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')


def mostrarReserva(request):
    reserva = tb_reserva.objects.all()
    contexto = {
        'reserva' : reserva
    }
    return render(request,'mostrarReserva.html',contexto)
    
def eliminarReserva(request,codigo):
    try:
        reserva = tb_reserva.objects.get(codigo_res = codigo)
        reserva.delete()
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def actualizaReserva(request,codigo):
    reserva = tb_reserva.objects.get(codigo_res = codigo)
    contexto = {
        'reserva' : reserva
    }
    return render(request, 'actualizarReserva.html',contexto)

def actualizarReserva(request):
    try:
        codigoRes = request.POST['codigoRes']
        fechaLlegada = request.POST['fechaLlegada']
        fechaSalida = request.POST['fechaSalida']
        cantidadJovenes = request.POST['cantidadJovenes']
        cantidadAdultos = request.POST['cantidadAdultos']

        if fechaLlegada<fechaSalida:
            reserva = tb_reserva.objects.get(codigo_res=codigoRes)

            reserva.fechaInicio_res = fechaLlegada
            reserva.fechaSalida_res = fechaSalida
            reserva.cantidadJovenes_res = cantidadJovenes
            reserva.cantidadAdultos_res = cantidadAdultos
        
            reserva.save()        
        else:
            return render(request,'errorReserva.html')
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    