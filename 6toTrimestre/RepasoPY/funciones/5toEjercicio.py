'''
Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el 
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y 
el mínimo, utilizando la función anterior.
'''

def calcularMaxMin(lista):
    numeroMayor = -999999999999999
    numeroMenor = 999999999999999
    for i in lista:
        if numeroMayor<i:
            numeroMayor = i        
        if numeroMenor>i:
            numeroMenor = i
    print(f'El numero menor de la lista es {numeroMenor}')        
    print(f'El numero mayor de la lista es {numeroMayor}')
          
print('-'*20,'MAXIMO Y MINIMO','-'*20)          

numeros = int(input('Cuantos numeros vas a ingresar?\n-'))
contador = 0
lista = []
print()
while True:
    numero = int(input('Ingresa un numero: '))
    lista.append(numero)    
    contador+=1
    if contador<numeros:        
        continue
    else:
        break    
print()     
calcularMaxMin(lista)