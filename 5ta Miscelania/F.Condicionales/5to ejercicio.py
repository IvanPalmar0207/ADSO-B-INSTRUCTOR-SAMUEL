'''Pida un numero al usuario que representa dias del año. Diga
a que mes del año corresponder asi. Si el numero es menor o igual
a 31 indica que esta en enero, Pero si el numero es 32 indica 
que es el 1 de Febrero. No tenga en cuenta si el año es bisiesto,
es decir febrero siempre tiene 28 dias.'''


def mes(numero=int(input("Ingrese un numero para calcular el mes: "))):
    if numero<=0:
        return "NO APLICA"
    elif numero<=31:
        return "Enero"
    elif numero >31 and numero <= 60:
        return "Febrero"
    elif numero >60 and numero <= 91:
        return "Marzo"
    elif numero > 91 and numero <= 121:
        return "Abril"
    elif numero > 121 and numero <= 152:
        return "Mayo"
    elif numero > 152 and numero <= 182:
        return "Junio"
    elif numero > 182 and numero <= 213:
        return "Julio"   
    elif numero > 213 and numero <= 244:
        return "Agosto"
    elif numero > 244 and numero <= 270:
        return "Septiembre"
    elif numero > 270 and numero <= 301:
        return "Octubre"
    elif numero > 301 and numero <=  331:
        return "Noviembre"
    elif numero > 331 and numero <= 365:
        return "Diciembre"
    else :
        return "ERROR"
print(mes()) 
                