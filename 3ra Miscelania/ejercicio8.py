'''Determinar cuales son los múltiplos de 5 comprendidos entre
1 y N.'''
num=int(input("ingrese un numero: "))
for i in range(1,num+1):
    if i%5==0:
        print(i,"es divisor de 5")