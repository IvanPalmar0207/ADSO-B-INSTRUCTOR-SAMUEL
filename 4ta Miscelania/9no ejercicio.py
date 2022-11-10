'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Encuentre la mediana de los números de la lista'''


import random
longi=0
mediana=int
tam=random.randint(10, 25)
vec=[]
for i in range(tam):
    vec.insert(i,round(random.randint(0, 100)))
print(vec)
longi=len(vec)
mediana=longi//2

if len(vec)%2==0:
    print('La mediana de los numeros de la lista es: ',vec[mediana-1], vec[mediana])
else:
    print('La mediana de los numeros de la lista es: ',vec[mediana])