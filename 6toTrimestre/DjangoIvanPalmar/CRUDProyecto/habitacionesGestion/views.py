from django.shortcuts import render, redirect
from habitacionesGestion.models import tb_habitacion,tb_mobiliario, tb_tipoHabitacion

# Create your views here.

def inicioHabitaciones(request):
    return render(request, 'tipoHabitacion.html')

def volver(request):
    return redirect('/')

def ingresarTipoHabitacion(request):
    try:
        codigoTipoHabitacion = request.POST['codigoTipoHabitacion']
        tipoHabitacion = request.POST['tipoHabitacion']
        valorBase = request.POST['valorBase']
        habitacion = tb_tipoHabitacion.objects.create(codigo_tpH = codigoTipoHabitacion, tipo_tpH = tipoHabitacion, valorBase_tpH = valorBase)
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def verTipoHabitacion(request):
    tipoHabitacion = tb_tipoHabitacion.objects.all()
    context = {
        'tipoHabitacion' : tipoHabitacion
    }
    return render(request, 'mostrarTipoHabitacion.html', context)
    
def eliminarTipoHabitacion(request,codigo):
    try:
        tipoHabitacion = tb_tipoHabitacion.objects.get(codigo_tpH = codigo)
        tipoHabitacion.delete()
    except Exception:
       return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def actualizaTipoHabitacion(request,codigo):
    tipoHabitacion = tb_tipoHabitacion.objects.get(codigo_tpH = codigo)
    contexto = {
        'tipoHabitacion':tipoHabitacion
    }
    return render(request,'actualizaTipoHabitacion.html',contexto)

def actualizarTipoHabitacion(request):
    try:
        codigoTipoHabitacion = request.POST['codigoTipoHabitacion']
        tipoHabitaciones = request.POST['tipoHabitacion']
        valorBase = request.POST['valorBase']
        
        tipoHabitacion = tb_tipoHabitacion.objects.get(codigo_tpH=codigoTipoHabitacion)
        
        tipoHabitacion.tipo_tpH = tipoHabitaciones
        tipoHabitacion.valorBase_tpH = valorBase

        tipoHabitacion.save()
        
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def mobiliario(request):
    tipoHabitacion = tb_tipoHabitacion.objects.all()
    contexto = {
        'tipoHabitacion': tipoHabitacion
    }
    
    return render(request,'mobiliario.html',contexto)

def insertarMobiliario(request):
    try:
        codigoTipoHabitacion = tb_tipoHabitacion.objects.get(codigo_tpH = request.POST['codigoTipoHabitacion'])
        camasSencillas = request.POST['camasSencillas']
        camasDobles = request.POST['camasDobles']
        camasTriples = request.POST['camasTriples']
        camasMatrimoniales = request.POST['camasMatrimoniales']
        numeroTelevisor = request.POST['numeroTelevisor']
        numeroBanos = request.POST['numeroBanos']
        numeroEscritorios = request.POST['numeroEscritorios']
        
        mobiliario = tb_mobiliario.objects.create(codigo_tpH = codigoTipoHabitacion,camasSecillas_im = camasSencillas, camasDobles_im = camasDobles, camasTriples_im = camasTriples, camasMatrimoniales_im = camasMatrimoniales, televisor_im = numeroTelevisor, bano_im = numeroBanos, escritorio_im = numeroEscritorios)
                
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def mostrarMobiliario(request):
    mobiliario = tb_mobiliario.objects.all()
    contexto = {
        'mobiliario' : mobiliario
    }
    return render(request,'mostrarMobiliario.html', contexto)

def eliminarMobiliario(request,codigo):
    try:
        mobiliario = tb_mobiliario.objects.get(id=codigo)
        mobiliario.delete()                
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def actualizaMobiliario(request,codigo):
    mobiliario = tb_mobiliario.objects.get(id = codigo)
    contexto = {
        'mobiliario' : mobiliario
    }
    return render(request,'actualizarMobiliario.html',contexto)

def actualizarMobiliario(request):
    try:
        codigoMobiliario = request.POST['codigoMobiliario']
        codigoTipoHabitacion = request.POST['codigoTipoHabitacion']
        camasSencillas = request.POST['camasSencillas']
        camasDobles = request.POST['camasDobles']
        camasTriples = request.POST['camasTriples']
        camasMatrimoniales = request.POST['camasMatrimoniales']
        numeroTelevisor = request.POST['numeroTelevisor']
        numeroBanos = request.POST['numeroBanos']
        numeroEscritorios = request.POST['numeroEscritorios']        

        mobiliario = tb_mobiliario.objects.get(id=codigoMobiliario)
        
        mobiliario.camasSecillas_im = camasSencillas
        mobiliario.camasDobles_im = camasDobles
        mobiliario.camasTriples_im = camasTriples
        mobiliario.camasMatrimoniales_im = camasMatrimoniales
        mobiliario.televisor_im = numeroTelevisor
        mobiliario.bano_im = numeroBanos
        mobiliario.escritorio_im = numeroEscritorios

        mobiliario.save()
        
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')

def habitaciones(request):
    tipoHabitacion = tb_tipoHabitacion.objects.all()
    contexto = {
        'tipoHabitacion' : tipoHabitacion
    }
    return render(request,'habitaciones.html',contexto)

def insertarHabitaciones(request):
    try:
        codigoHabitacion = request.POST['codigoHabitacion']
        codigoTipoHabitacion = tb_tipoHabitacion.objects.get(codigo_tpH = request.POST['codigoTipo'])
        precioHabitacion = request.POST['precioHabitacion']
        descripcionHabitacion = request.POST['descripcionHabitacion']
        minimoPersonas = request.POST['minimoPersonas']
        maximoPersonas = request.POST['maximoPersonas']
        imagenHabitacion = request.POST['imagenHabitacion']
        
        habitaciones = tb_habitacion.objects.create(codigo_hab = codigoHabitacion, codigo_tpH = codigoTipoHabitacion, precio_tpH = precioHabitacion, descripcion_tpH = descripcionHabitacion, minimoPersonas_tpH = minimoPersonas, maximoPersonas_tpH = maximoPersonas, image_tpH = imagenHabitacion)
                
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def mostrarHabitaciones(request):
    habitaciones = tb_habitacion.objects.all()
    contexto = {
        'habitaciones' : habitaciones
    }
    return render(request,'mostrarHabitaciones.html',contexto)

def eliminarHabitaciones(request,codigo):
    try:
        habitaciones = tb_habitacion.objects.get(codigo_hab = codigo)
        habitaciones.delete()
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def actualizaHabitaciones(request,codigo):
    habitaciones = tb_habitacion.objects.get(codigo_hab = codigo)
    tipoHabitacion = tb_tipoHabitacion.objects.all()
    contexto = {
        'habitaciones' : habitaciones,
        'tipoHabitacion' : tipoHabitacion
    }
    return render(request,'actualizarHabitaciones.html',contexto)
        
def actualizarHabitaciones(request):
    try:
        codigoHabitacion = request.POST['codigoHabitacion']
        codigoTipo = tb_tipoHabitacion.objects.get(codigo_tpH=request.POST['codigoTipo'])
        precioHabitacion = request.POST['precioHabitacion']
        descripcionHabitacion = request.POST['descripcionHabitacion']
        minimoPersonas = request.POST['minimoPersonas']
        maximoPersonas = request.POST['maximoPersonas']

        habitaciones = tb_habitacion.objects.get(codigo_hab=codigoHabitacion)
        
        habitaciones.codigo_tpH = codigoTipo
        habitaciones.precio_tpH = precioHabitacion
        habitaciones.descripcion_tpH = descripcionHabitacion
        habitaciones.minimoPersonas_tpH = minimoPersonas
        habitaciones.maximoPersonas_tpH = maximoPersonas
        
        habitaciones.save()        
    
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')