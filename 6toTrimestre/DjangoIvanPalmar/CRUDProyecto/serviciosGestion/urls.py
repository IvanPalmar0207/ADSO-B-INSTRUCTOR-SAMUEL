from django.urls import path
from serviciosGestion.views import inicioServicios, insertarCategoria,verCategorias,eliminarCategoria, actualizaCategoria,actualizarHabitacion,ingresaServicios,insertarServicios, verServicios, eliminarServicio,actualizaServicio,actualizarServicio,ingresarConsumos, insertarConsumos, verConsumos, eliminarConsumo, actualizaConsumo, actualizarConsumo


urlpatterns = [
    path('inicioServicios', inicioServicios, name = 'inicioServicios'),
    path('insertarCategoria/',insertarCategoria, name = 'insertarCategoria'),
    path('verCategorias',verCategorias, name = 'verCategorias'),
    path('eliminarCategoria/<codigoCat>',eliminarCategoria, name = 'eliminarCategoria'),
    path('actualizaCategoria/<codigoCat>',actualizaCategoria, name = 'actualizaCategoria'),
    path('actualizaCategoria/actualizarHabitacion/',actualizarHabitacion, name = 'actualizarHabitacion'),
    path('ingresaServicios',ingresaServicios, name='ingresaServicios'),
    path('insertarServicios/',insertarServicios,name='insertarServicios'),
    path('verServicios', verServicios, name = 'verServicios'),
    path('eliminarServicio/<codigo>', eliminarServicio, name = 'eliminarServicio'),
    path('actualizaServicio/<codigo>', actualizaServicio, name = 'actualizaServicio'),
    path('actualizaServicio/actualizarServicio/', actualizarServicio, name = 'actualizarServicio'),
    path('ingresarConsumos', ingresarConsumos, name = 'ingresarConsumos'),
    path('insertarConsumos/', insertarConsumos, name = 'insertarConsumos'),
    path('verConsumos', verConsumos, name = 'verConsumos'),
    path('eliminarConsumo/<codigo>', eliminarConsumo, name = 'eliminarConsumo'),
    path('actualizaConsumo/<codigo>', actualizaConsumo, name = 'actualizaConsumo'),
    path('actualizaConsumo/actualizarConsumo/', actualizarConsumo, name = 'actualizarConsumo')
]
