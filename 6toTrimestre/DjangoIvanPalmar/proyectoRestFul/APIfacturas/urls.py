from django.urls import path,include
from APIfacturas.views import moduloFacturasAPI
from APIfacturas.views import facturasViewSet, metodoPagoViewSet
from rest_framework import routers

routerFacturas = routers.DefaultRouter()
routerFacturas.register(r'facturas', facturasViewSet)

routerMetodoPago = routers.DefaultRouter()
routerMetodoPago.register(r'metodoPago',metodoPagoViewSet)

urlpatterns = [
    path('', moduloFacturasAPI, name = 'moduloFacturasAPI'),
    path('apiFacturas/',include(routerFacturas.urls)),
    path('apiMetodoPago/', include(routerMetodoPago.urls))
]
