from django.urls import path
from gestionaprendices.views import listaAprendices

urlpatterns = [
    path('lista', listaAprendices, name='lista_Aprendices')
]