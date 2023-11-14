from django.shortcuts import render,redirect
from usuariosGestion.models import tb_rol, tb_tpDocumento, tb_usuarios

# Create your views here.

def registrarse(request):
    rol = tb_rol.objects.all()
    tipoDocumento = tb_tpDocumento.objects.all()
    
    context ={
        'tipoDocumento': tipoDocumento,
        'rol' : rol
    }
    
    return render(request,'registrarse.html',context)

def volver(request):
    return redirect('/')

def registrarUsuario(request):
    try:
        numeroDoc = request.POST['numeroDoc']
        tipoDoc = tb_tpDocumento.objects.get(codigo_tpD=request.POST['tipoDoc'])
        email = request.POST['email']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rol = tb_rol.objects.get(codigo_rl=request.POST['rol'])
        contrasena = request.POST['contrasena']
        usuario = tb_usuarios.objects.create(numeroDocumento_cli = numeroDoc, correoElectronico_clI = email, nombres_cli = nombre, apellidos_cli = apellido, contrasena_cli = contrasena, codigo_tpD = tipoDoc, codigo_rl = rol)
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')

def verUsuarios(request):
    usuario = tb_usuarios.objects.all()
    context = {
        'usuarios' : usuario
    }
    return render (request,'verUsuarios.html',context)

def volverVer(request):
    return render(request,'registrarse.html')

def eliminarUsuario(request,numeroDoc):
    try:
        usuario = tb_usuarios.objects.get(numeroDocumento_cli=numeroDoc)
        usuario.delete()
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')

def actualizaUsu(request,numeroDoc):
    usuario = tb_usuarios.objects.get(numeroDocumento_cli=numeroDoc)
    rol = tb_rol.objects.all()
    contexto = {
        'usuario':usuario,
        'rol':rol
    }
    return render(request,'actualizaUsu.html',contexto)
    
def actualizarUsuario(request):
    try:
        numeroDoc = request.POST['numeroDoc']
        email = request.POST['email']
        nombre = request.POST['nombre_cli']
        apellido = request.POST['apellido']
        rol = tb_rol.objects.get(codigo_rl=request.POST['rol'])
        contrasena = request.POST['contrasena']
        
        usuario = tb_usuarios.objects.get(numeroDocumento_cli=numeroDoc)
        
        usuario.correoElectronico_clI = email
        usuario.nombres_cli = nombre
        usuario.apellidos_cli = apellido
        usuario.codigo_rl = rol
        usuario.contrasena_cli = contrasena
        
        usuario.save()
        
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')