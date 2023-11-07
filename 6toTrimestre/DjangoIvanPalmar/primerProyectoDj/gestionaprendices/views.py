from django.shortcuts import render
from gestionaprendices.models import Aprendiz

# Create your views here.

def listaAprendices(request):
    getAprendiz = Aprendiz.objects.all()
    data = {
        'getAprendices':getAprendiz
    }

    return render(request,'listaAprendices.html',data)