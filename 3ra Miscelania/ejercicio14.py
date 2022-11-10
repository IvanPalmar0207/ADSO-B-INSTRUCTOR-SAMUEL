'''Calcular todos los números de 3 cifras tales que la suma
de los cubos de las cifras es igual al valor del número.'''

for n in range (100,1000):
    d=0
    suma=0
    i=n
    while i > 0:
        x=i%10
        z=i//10
        d=x**3
        suma+= d
        i=z
    if suma == n:
        print("Los siquientes numeros cumplen con las condiciones: ",n )