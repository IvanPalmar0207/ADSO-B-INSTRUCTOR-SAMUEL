from django.urls import path
from serviciosGestion.views import inicioServicios, insertarCategoria,verCategorias,eliminarCategoria, actualizaCategoria,actualizarHabitacion,ingresaServicios,insertarServicios


urlpatterns = [
    path('inicioServicios', inicioServicios, name = 'inicioServicios'),
    path('insertarCategoria/',insertarCategoria, name = 'insertarCategoria'),
    path('verCategorias',verCategorias, name = 'verCategorias'),
    path('eliminarCategoria/<codigoCat>',eliminarCategoria, name = 'eliminarCategoria'),
    path('actualizaCategoria/<codigoCat>',actualizaCategoria, name = 'actualizaCategoria'),
    path('actualizaCategoria/actualizarHabitacion/',actualizarHabitacion, name = 'actualizarHabitacion'),
    path('ingresaServicios',ingresaServicios, name='ingresaServicios'),
    path('insertarServicios/',insertarServicios,name='insertarServicios')
]
