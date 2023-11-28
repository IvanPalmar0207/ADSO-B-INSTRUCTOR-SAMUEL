from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from usuariosAPI.serializers import tb_rolSerializer, tb_tpDocumentoSerializer, tb_usuariosSerializer
from usuariosAPI.models import tb_rol, tb_usuarios, tb_tpDocumento

# Create your views here.

#Pagina principal de usuarios

def gestionUsuariosPrincipal(request):
    return render(request,'gestionUsuarios.html')

#CRUD para Usuarios

@api_view(['GET'])
def usuariosOperaciones(request):
    apiUrls = {
        'Todos los usuarios' : '/usuariosTodos/',
        'Solo un usuario' : '/usuariosUno/<numeroDocumento>',
        'Crear Usuario' : '/usuariosCrear/',
        'Actualizar Usuario' : '/usuarioActualizar/<numeroDocumento>',
        'Eliminar Usuario' : '/usuarioEliminar/<numeroDocumento>',
    }
    return Response(apiUrls)

@api_view(['GET'])
def usuariosTodos(request):
    try:
        usuarios = tb_usuarios.objects.all()
        serializador = tb_usuariosSerializer(usuarios, many = True)
    except Exception:
        return redirect(usuariosOperaciones)
    else:
        return Response(serializador.data)

@api_view(['GET'])
def usuariosUno(request, numeroDocumento):
    try:
        usuarios = tb_usuarios.objects.get(numeroDocumento_cli=numeroDocumento)
        serializador = tb_usuariosSerializer(usuarios, many = False)
    except Exception:
        return redirect(usuariosOperaciones)
    else:
        return Response(serializador.data)
    
@api_view(['POST'])
def usuariosCrear(request):
    serializador = tb_usuariosSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(serializador.data)
    else:
        return redirect(usuariosOperaciones)
    
@api_view(['PUT','PATCH'])
def usuarioActualizar(request,numeroDocumento):
    usuario = tb_usuarios.objects.get(numeroDocumento_cli=numeroDocumento)
    serializador = tb_usuariosSerializer(instance = usuario, data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(serializador.data)
    else:
        return redirect(usuariosOperaciones)

@api_view(['DELETE'])        
def usuarioEliminar(request, numeroDocumento):
    try:
        usuario = tb_usuarios.objects.get(numeroDocumento_cli=numeroDocumento)
        usuario.delete()
    except Exception:
        return redirect(usuariosOperaciones)
    else: 
        return redirect(usuariosOperaciones)

#CRUD para tipos de Documento

@api_view(['GET'])
def tipoDocumentoOperaciones(request):
    
    apiUrls = {
        'Todos los Tp.Documento' : '/tipoDocTodos/',
        'Solo un Tp.Documento' : '/tipoDocUno/<id>',
        'Agregar un Tp.Documento' : '/tipoDocAgregar/',
        'Actualizar Tp.Documento' : '/tipoDocActualizar/<id>',
        'Elimnar Tp.Documento' : '/tipoDocEliminar/<id>'
    }
    
    return Response(apiUrls)

@api_view(['GET'])
def tipoDocTodos(request):
    try:        
        tiposDocumento = tb_tpDocumento.objects.all()
        serializador = tb_tpDocumentoSerializer(tiposDocumento, many = True)
    except Exception:
        return redirect(tipoDocumentoOperaciones)
    else:
        return Response(serializador.data)
        
@api_view(['GET'])
def tipoDocUno(request,id):
    try:
        tiposDocumento = tb_tpDocumento.objects.get(codigo_tpD=id)
        serializador = tb_tpDocumentoSerializer(tiposDocumento, many = False)
    except Exception:
        return redirect(tipoDocumentoOperaciones)
    else:
        return Response(serializador.data)

@api_view(['POST'])
def tipoDocAgregar(request):    
    serializador = tb_tpDocumentoSerializer(data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(serializador.data)
    else:
        return redirect(tipoDocumentoOperaciones)


@api_view(['PUT','PATCH'])
def tipoDocActualizar(request,id):
    tipoDocumento = tb_tpDocumento.objects.get(codigo_tpD=id)
    serializador = tb_tpDocumentoSerializer(instance = tipoDocumento, data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(serializador.data)
    else:
        return redirect(tipoDocumentoOperaciones)


@api_view(['DELETE'])
def tipoDocEliminar(request,id):
    try:
        tipoDocumento = tb_tpDocumento.objects.get(codigo_tpD=id)
    except Exception:
        return redirect(tipoDocumentoOperaciones)
    else:
        tipoDocumento.delete()
        return redirect(tipoDocumentoOperaciones)
    
    
#CRUD para tipos de rol

@api_view(['GET'])
def rolOperaciones(request):
    
    apiRuls = {
        'Todos los roles' : '/rolTodos/',
        'Solo un rol' : '/rolUno/<id>',
        'Crear un rol' : '/rolAgregar/',
        'Actualizar rol' : '/rolActualizar/<id>',
        'Eliminar rol' : '/rolEliminar/<id>'
    }
    
    return Response(apiRuls)

@api_view(['GET'])
def rolTodos(request):
    try:
        rol = tb_rol.objects.all()
        serializador = tb_rolSerializer(rol, many = True)
    except Exception:
        return redirect(rolOperaciones)
    else:
        return Response(serializador.data)

@api_view(['GET'])
def rolUno(request,id):
    try:
        rol = tb_rol.objects.get(codigo_rl=id)
        serializador = tb_rolSerializer(rol, many = False)
    except Exception:
        return redirect(rolOperaciones)
    else:
        return Response(serializador.data)
    
@api_view(['POST'])
def rolAgregar(request):
    rol = tb_rolSerializer(data = request.data)
    if rol.is_valid():
        rol.save()
        return Response(rol.data)
    else:
        return redirect(rolOperaciones)
    
@api_view(['PUT','PATCH'])
def rolActualizar(request,id):    
    rol = tb_rol.objects.get(codigo_rl=id)
    serializador = tb_rolSerializer(instance = rol, data = request.data)
    if serializador.is_valid():
        serializador.save()
        return Response(serializador.data)
    else:
        return redirect(rolOperaciones)
    
@api_view(['DELETE'])
def rolEliminar(request,id):
    try:
        rol = tb_rol.objects.get(codigo_rl=id)
        rol.delete()
    except Exception:
        return redirect(rolOperaciones)
    else:
        return redirect(rolOperaciones)        