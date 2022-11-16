'''Pedir un numero entre 0 y 9.999 y decir cuantas
cifras tiene. Cuando el numero exceda los limites 
emita un mensaje y finalice el programa'''

def cifras(numero=float(input("Digita tu numero: "))):

    if numero < 0:
        return "El numero es negativo"
    elif numero <=9:
        return "El numero es de una cifra"
    elif numero <=99:
        return "El numero es de dos cifras"   
    elif numero <=999:
        return "El numero es de tres cifras"
    elif numero<=9999:
        return "El numero es de cuatro cifras"
    else:
        return "!ERRORRR¡"

print(cifras())