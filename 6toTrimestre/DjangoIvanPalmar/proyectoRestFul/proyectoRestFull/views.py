from django.shortcuts import render

def paginaPrincipal(request):
    return render(request,'paginaPrincipal.html')