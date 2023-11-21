from django.urls import path
from usuariosGestion.views import registrarse,volver,registrarUsuario,verUsuarios,volverVer, eliminarUsuario,actualizaUsu, actualizarUsuario, iniciarSesion, iniciarSesionIngresar
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('registrarse',registrarse,name='registrarse'),
    path('volver',volver,name='volver'),
    path('registrarUsuario/',csrf_exempt(registrarUsuario),name='registrarUsuario'),
    path('verUsuarios',csrf_exempt(verUsuarios), name='verUsuarios'),
    path('volverVer', volverVer,name='volverVer'),
    path('eliminarUsuario/<numeroDoc>',csrf_exempt(eliminarUsuario)),
    path('actualizaUsu/<numeroDoc>',csrf_exempt(actualizaUsu)),
    path('actualizaUsu/actualizarUsuario/',csrf_exempt(actualizarUsuario),name='actualizarUsuario'),
    path('iniciarSesion',iniciarSesion,name='iniciarSesion'),
    path('iniciarSesionIngresar/',iniciarSesionIngresar,name='iniciarSesionIngresar')
]