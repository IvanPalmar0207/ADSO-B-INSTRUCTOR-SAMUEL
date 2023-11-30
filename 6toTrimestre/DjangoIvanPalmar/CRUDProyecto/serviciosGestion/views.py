from django.shortcuts import render
from serviciosGestion.models import tb_categoria, tb_servicio

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
    