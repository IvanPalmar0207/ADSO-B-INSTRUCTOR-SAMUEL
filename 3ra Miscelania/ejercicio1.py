'''Determinar los divisores de un número introducido por
teclado'''
numero = int(input("introduzca el numero: "))
for i in range(1,numero+1):
    if (numero % i) == 0 :
        print(i,"es divisor de:",numero)