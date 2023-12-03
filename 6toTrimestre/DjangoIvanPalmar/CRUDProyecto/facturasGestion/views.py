from django.shortcuts import render
from facturasGestion.models import tb_metodoPago, tb_reserva, tb_factura
from serviciosGestion.models import tb_consumo

# Create your views here.

def inicioFacturas(request):
    metodoPago = tb_metodoPago.objects.all()
    reservas = tb_reserva.objects.all()
    consumo = tb_consumo.objects.filter(codigo_res = 10)
    
    contexto = {
        'metodoPago' : metodoPago
    }
    
    return render(request, 'inicioFacturas.html', contexto)

def agregarFactura(request):
    try:
        codigoFactura = request.POST['codigoFactura']
        codigoReserva = tb_reserva(codigo_res = request.POST['codigoReserva'])
        metodoPago1 = request.POST['metodoPago1']
        metodoPago2 = request.POST['metodoPago2']

        consumo = tb_consumo.objects.filter(codigo_res = codigoReserva)
    
        precio = 0 
        for i in consumo:
            precio += i.precioUnitario_con * i.cantidad_con

        if metodoPago2 == "vacio":
            factura = tb_factura.objects.create(codigo_fac = codigoFactura, codigo_res = codigoReserva, valorTotal_fac = precio)
            factura.codigo_mP.add(metodoPago1)
            for i in consumo:
                factura.numero_con.add(i.numero_con)
            factura.save()
        else:
            factura = tb_factura.objects.create(codigo_fac = codigoFactura, codigo_res = codigoReserva, valorTotal_fac = precio)
            factura.codigo_mP.add(metodoPago1)
            factura.codigo_mP.add(metodoPago2)        
            for i in consumo:
                factura.numero_con.add(i.numero_con)
            factura.save()
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')
    
def verFacturas(request):
    try:
        facturas = tb_factura.objects.all()
        contexto = {
            'facturas' : facturas
        }
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'mostrarFacturas.html', contexto)
    
def eliminarFacturas(request, codigo):
    try:
        facturas = tb_factura.objects.get(codigo_fac = codigo)    
        facturas.delete()
    except Exception:
        return render(request, 'errorUsuario.html')
    else:
        return render(request, 'volverRegistro.html')