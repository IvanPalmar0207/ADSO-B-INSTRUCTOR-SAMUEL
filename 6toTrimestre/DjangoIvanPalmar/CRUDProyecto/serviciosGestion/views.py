from django.shortcuts import render
from serviciosGestion.models import tb_categoria, tb_servicio, tb_consumo, tb_reserva

# Create your views here.

def inicioServicios(request):
    return render(request,'inicioServicios.html')

#CRUD de categoria

def insertarCategoria(request):
    try:
        codigoCategoria = request.POST['codigoCategoria']
        nombreCategoria = request.POST['nombreCategoria']
        descripcionCategoria = request.POST['descripcionCategoria']
        imagenCategoria = request.POST['imagenCategoria']
        
        categoria = tb_categoria.objects.create(codigo_cat = codigoCategoria, nombre_cat = nombreCategoria, descripcion_cat = descripcionCategoria, imagen_cat = imagenCategoria)
        
    except Exception:
        return render(request,'errorUsuario.html')
    else:
        categoria.save()
        return render(request,'volverRegistro.html')
    
def verCategorias(request):
    categorias = tb_categoria.objects.all()
    contexto = {
        'categorias': categorias
    }
    return render(request,'mostrarCategorias.html', contexto)

def eliminarCategoria(request,codigoCat):
    try:
        categoria = tb_categoria.objects.get(codigo_cat = codigoCat)
        categoria.delete()
    except Exception:
        return render(request,'errorUsuario.html')        
    else:
        return render(request,'volverRegistro.html')        
    
def actualizaCategoria(request, codigoCat):
    try:
        categoria = tb_categoria.objects.get(codigo_cat = codigoCat)
        contexto = {
            'categoria' : categoria
        }
    except Exception:
        return render(request,'errorUsuario.html')                
    else:
        return render(request,'actualizarCategoria.html', contexto)
    
def actualizarHabitacion(request):
    try:
        codigoCategoria = request.POST['codigoCategoria']
        nombreCategoria = request.POST['nombreCategoria']
        descripcionCategoria = request.POST['descripcionCategoria']
        
        categoria = tb_categoria.objects.get(codigo_cat=codigoCategoria)
        
        categoria.nombre_cat = nombreCategoria
        categoria.descripcion_cat = descripcionCategoria

        categoria.save()
        
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
#CRUD de los servicios

def ingresaServicios(request):
    categoria  = tb_categoria.objects.all()
    contexto ={
        'categoria' : categoria
    }
    return render(request,'insertarServicios.html',contexto)

def insertarServicios(request):
    try:
        codigoServicio = request.POST['codigoServicio']
        nombreServicio = request.POST['nombreServicio']
        descripcionServicio = request.POST['descripcionServicio']
        imagenServicio = request.POST['imagenServicio']
        codigoCategoria = tb_categoria.objects.get(codigo_cat=request.POST['codigoCategoria'])
        
        servicio = tb_servicio.objects.create(codigo_ser = codigoServicio, nombre_ser = nombreServicio, descripcion_ser = descripcionServicio, imagen_ser = imagenServicio, codigo_cat = codigoCategoria)
        
    except Exception:
        return render(request,'errorUsuario.html')
    else:
        servicio.save()
        return render(request,'volverRegistro.html')
    
def verServicios(request):
    try:
        servicios = tb_servicio.objects.all()
        contexto = {
            'servicios' : servicios
        }
    except Exception:
        return render(request,'errorUsuario.html')        
    else:
        return render(request,'mostrarServicios.html',contexto)
    
def actualizaServicio(request,codigo):
    try:
        servicio = tb_servicio.objects.get(codigo_ser = codigo)
        categoria = tb_categoria.objects.all()
        contexto = {
            'servicios' : servicio,
            'categoria' : categoria
        }
    except Exception:
        return render(request,'errorUsuario.html')        
    else:
        return render(request,'actualizarServicio.html',contexto)

def actualizarServicio(request):
    try:
        codigoServicio = request.POST['codigoServicio']
        nombreServicio = request.POST['nombreServicio']
        descripcionServicio = request.POST['descripcionServicio']
        codigoCategoria = tb_categoria.objects.get(codigo_cat = request.POST['codigoCategoria'])
        
        servicio = tb_servicio.objects.get(codigo_ser = codigoServicio)
        
        servicio.nombre_ser = nombreServicio
        servicio.descripcion_ser = descripcionServicio
        servicio.codigo_cat = codigoCategoria
        servicio.save()        
    except Exception:
        return render(request,'errorUsuario.html')
    else:
        servicio.save()
        return render(request,'volverRegistro.html')
        
    
def eliminarServicio(request, codigo):
    try:
        servicio = tb_servicio.objects.get(codigo_ser = codigo)        
        servicio.delete()
    except Exception:
        return render(request,'errorUsuario.html')        
    else:    
        return render(request, 'volverRegistro.html')
    
def ingresarConsumos(request):
    reservas = tb_reserva.objects.all()
    servicios = tb_servicio.objects.all()
    contexto = {
        'reservas' : reservas,
        'servicios' : servicios
    }
    return render(request,'ingresarConsumos.html', contexto)

def insertarConsumos(request):    
    try:
        codigoReserva = tb_reserva.objects.get(codigo_res = request.POST['codigoReserva'])
        codigoServicio = tb_servicio.objects.get(codigo_ser = request.POST['codigoServicio'])
        fechaConsumo = request.POST['fechaConsumo']
        cantidadConsumo = request.POST['cantidadConsumo']
        precioUnitarioConsumo = request.POST['precioUnitarioConsumo']
        
        consumos = tb_consumo(codigo_res = codigoReserva, codigo_ser = codigoServicio, fecha_con = fechaConsumo, cantidad_con = cantidadConsumo, precioUnitario_con = precioUnitarioConsumo)
        consumos.save()
    except Exception:
        return render(request,'errorUsuario.html')
    else:
        return render(request,'volverRegistro.html')
    
def verConsumos(request):
    try:
        consumos = tb_consumo.objects.all()
        contexto = {
            'consumos' : consumos
        }
    except Exception:
        return render(request,'errorUsuario.html')        
    else:
        return render(request,'verConsumos.html',contexto)
    
def actualizaConsumo(request,codigo):
    try:
        consumos = tb_consumo.objects.get(numero_con = codigo)
        servicios = tb_servicio.objects.all()
        contexto ={
            'consumos' : consumos,
            'servicios' : servicios
        }
    except Exception:
        return render(request,'errorUsuario.html')        
    else:
        return render(request,'actualizarConsumo.html', contexto)
    
def actualizarConsumo(request):
    try:
        codigoServicio = tb_servicio.objects.get(codigo_ser = request.POST['codigoServicio'])
        fechaConsumo = request.POST['fechaConsumo']
        cantidadConsumo = request.POST['cantidadConsumo']
        precioUnitarioConsumo = request.POST['precioUnitarioConsumo']
        numeroConsumo = request.POST['numeroConsumo']
        
        consumo = tb_consumo.objects.get(numero_con = numeroConsumo)
        
        consumo.codigo_ser = codigoServicio
        consumo.fecha_con = fechaConsumo
        consumo.cantidad_con = cantidadConsumo
        consumo.precioUnitario_con = precioUnitarioConsumo
                
        consumo.save()        
    except Exception:
        return render(request,'errorUsuario.html')
    else:
        return render(request,'volverRegistro.html')
    
def eliminarConsumo(request, codigo):
    try:
        consumo = tb_consumo.objects.get(numero_con = codigo)
        consumo.delete()
    except Exception:
        return render(request,'errorUsuario.html')        
    else:    
        return render(request, 'volverRegistro.html')