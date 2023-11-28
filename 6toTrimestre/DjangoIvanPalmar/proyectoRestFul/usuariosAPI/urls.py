from django.urls import path
from usuariosAPI.views import usuariosOperaciones, gestionUsuariosPrincipal, tipoDocumentoOperaciones,rolOperaciones, tipoDocTodos, tipoDocUno,tipoDocAgregar, tipoDocEliminar, tipoDocActualizar
from usuariosAPI.views import rolTodos, rolUno, rolAgregar, rolActualizar,rolEliminar
from usuariosAPI.views import usuariosTodos, usuariosUno, usuariosCrear, usuarioActualizar, usuarioEliminar

urlpatterns = [
    path('gestionUsuariosPrincipal',gestionUsuariosPrincipal,name='gestionUsuariosPrincipal'),
    path('usuariosOperaciones/', usuariosOperaciones, name = 'usuariosOperaciones'),
    path('tipoDocumentoOperaciones/',tipoDocumentoOperaciones,name = 'tipoDocumentoOperaciones'),
    path('rolOperaciones/',rolOperaciones , name = 'rolOperaciones'),
    path('tipoDocTodos/',tipoDocTodos, name = 'tipoDocTodos'),
    path('tipoDocUno/<id>',tipoDocUno, name = 'tipoDocUno'),
    path('tipoDocAgregar/',tipoDocAgregar, name = 'tipoDocAgregar'),
    path('tipoDocEliminar/<id>', tipoDocEliminar, name = 'tipoDocEliminar'),
    path('tipoDocActualizar/<id>',tipoDocActualizar, name = 'tipoDocActualizar'),
    path('rolTodos/', rolTodos, name = 'rolTodos'),
    path('rolUno/<id>', rolUno, name = 'rolUno'),
    path('rolAgregar/', rolAgregar, name = 'rolAgregar'),
    path('rolActualizar/<id>', rolActualizar, name = 'rolActualizar'),
    path('rolEliminar/<id>', rolEliminar, name = 'rolEliminar'),
    path('usuariosTodos/', usuariosTodos, name = 'usuariosTodos'),
    path('usuariosUno/<numeroDocumento>', usuariosUno, name = 'usuariosUno'),
    path('usuariosCrear/', usuariosCrear , name = 'usuariosCrear'),
    path('usuarioActualizar/<numeroDocumento>', usuarioActualizar, name = 'usuarioActualizar'),
    path('usuarioEliminar/<numeroDocumento>', usuarioEliminar, name = 'usuarioEliminar')
]