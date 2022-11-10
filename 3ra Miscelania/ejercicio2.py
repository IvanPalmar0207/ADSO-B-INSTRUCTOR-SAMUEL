'''Determinar si el numero es o no es par'''
num=2
while num%2==0:
    print(num,"es par")
    num=int(input("Ingrese un numero: "))
else:
    print(num,"no es par")