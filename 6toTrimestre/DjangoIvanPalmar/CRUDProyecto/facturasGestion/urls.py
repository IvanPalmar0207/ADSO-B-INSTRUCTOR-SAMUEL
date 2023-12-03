from django.urls import path
from facturasGestion.views import inicioFacturas, agregarFactura, verFacturas, eliminarFacturas

urlpatterns = [
    path('inicioFacturas',inicioFacturas, name = 'inicioFacturas'),
    path('verFacturas', verFacturas, name = 'verFacturas'),
    path('agregarFactura/', agregarFactura, name = 'agregarFactura'),
    path('eliminarFacturas/<codigo>', eliminarFacturas, name = 'eliminarFacturas')
]
