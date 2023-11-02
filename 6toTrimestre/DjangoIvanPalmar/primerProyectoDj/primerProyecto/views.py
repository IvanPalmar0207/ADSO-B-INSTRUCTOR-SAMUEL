from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def iniciarSesion(request):
    return render(request,'iniciarSesion.html')

def registrarse(request):
    return render(request,'registrarse.html')

def paginaPrincipal(request):
    return render(request,'paginaPrincipal.html')

def reservar(request):
    return render(request,'reserva.html')

def servicios(request):
    return render(request,'servicios.html')