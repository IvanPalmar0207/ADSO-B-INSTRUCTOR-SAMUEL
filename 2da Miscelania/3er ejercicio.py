'''Pedir un numero entre 0 y 9.999 y decir cuantas
cifras tiene. Cuando el numero exceda los limites 
emita un mensaje y finalice el programa'''

numero=float(input("Digita tu numero: "))

if numero <=9:
    print("El numero es de 1 cifra")
elif numero <=99:
    print("El numero es de 2 cifras")    
elif numero <=999:
    print("El numero es de 3 cifras")
elif numero<=9999:
    print("El numero es de 4 cifras")
else:
    print("!ERRORRR¡")    