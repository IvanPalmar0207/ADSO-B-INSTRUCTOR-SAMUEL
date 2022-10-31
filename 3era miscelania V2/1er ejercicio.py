'''Pedir numero e imprimirlos con el opuesto'''

n=1
contador=0

while n!=0:
    n=int(input("Ingresa un numero: "))
    if n!=0:
        print(n,"opuesto de", -(n))
        contador+=1
    if n == 0:
        print("El prgrama ha finalizado porque el numero es igual a 0")