'''Determinar los divisores de un numero
introducido por teclado'''

numero=int(input("Ingresa el numero: "))

x=1
while x <= numero:
    if numero % x == 0:
        print("El numero",numero,"es divisible entre",x)
    x=x+1
print("Ya pudiste visualizar los distintos divisores")