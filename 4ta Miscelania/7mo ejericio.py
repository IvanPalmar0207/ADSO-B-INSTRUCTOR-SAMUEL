'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la suma y el promedio de los números de la lista'''

import random

cont=0
prom=0
suma1=0
tam=random.randint(10, 25)
vec=[]
for i in range(tam):
    vec.insert(i,round(random.randint(0, 100)))
print(vec)

for i in range(len(vec)):
    cont=cont+1
    suma1=suma1+vec[i]
    prom=suma1/cont

print('La suma de los numeros de la lista  es: ',suma1)
print('El promedio de los numeros de la lista es: ',prom)
