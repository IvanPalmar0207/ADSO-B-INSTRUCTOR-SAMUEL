'''Determinar si un numero es o no es primo'''
numero=int(input("Ingresa un numero: "))
x=1
c=0
while x<=numero:
    if numero % x == 0:
        c = c + 1
    x = x + 1
if c==2:
    print("El numero", numero, "es primo")
else:
    print("El numero ", numero, "no es primo")