from django.urls import path
from usuariosGestion.views import registrarse,volver,registrarUsuario,verUsuarios,volverVer, eliminarUsuario,actualizaUsu, actualizarUsuario

urlpatterns = [
    path('registrarse',registrarse,name='registrarse'),
    path('volver',volver,name='volver'),
    path('registrarUsuario/',registrarUsuario,name='registrarUsuario'),
    path('verUsuarios',verUsuarios, name='verUsuarios'),
    path('volverVer', volverVer,name='volverVer'),
    path('eliminarUsuario/<numeroDoc>',eliminarUsuario),
    path('actualizaUsu/<numeroDoc>',actualizaUsu),
    path('actualizaUsu/actualizarUsuario/',actualizarUsuario,name='actualizarUsuario')
]
