'''Determinar si un número es o no es perfecto. Un numero es
perfecto si la suma de sus divisores sin incluir el propio
número es igual a este'''
numero = int(input("introduzca el numero: "))
i=1
divisores=0
for i in range(1,numero):
    if (numero % i) == 0 :
        divisores=divisores+i
if divisores==numero:
    print("es numero perfecto")
else:
    print("no es numero perfecto")