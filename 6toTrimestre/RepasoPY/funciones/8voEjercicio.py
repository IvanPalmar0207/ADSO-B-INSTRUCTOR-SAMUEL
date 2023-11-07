'''
Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal
donde se lea un entero y se muestre el resultado del factorial.
'''

def factorialNumero(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorialNumero(numero-1)

print('-'*20,'FACTORIAL DE UN NUMERO','-'*20)
print()
numero = int(input('Ingresa un numero: '))
print(f'El factorial del numero {numero} es igual a {factorialNumero(5)}')    