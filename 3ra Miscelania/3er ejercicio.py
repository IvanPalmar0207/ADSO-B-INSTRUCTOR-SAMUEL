'''Determinar si un numero es o no es perfecto. Un numero es perfecto si
la suma de sus divisores sin incluir el propio numero es igual a este'''
Numero=int(input("Ingresa la cantidad de numeros que deseas evaluar: "))
for i in range(2, Numero+1):
    b=0
    for j in range(1, (i//2)+1):
        if((i%j)==0):
            b= b+j;
    if(b==i):
        print("%s es perfecto" %i)
    else:
        print("%s no es perfecto" %i)