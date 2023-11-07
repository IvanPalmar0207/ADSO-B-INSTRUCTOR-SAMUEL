'''
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es 
múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve 
si el primero es múltiplo del segundo.
'''

print('-'*20,'MULTIPLOS - DOS NUMEROS','-'*20)
numero1 = int(input('Ingresa el primer numero: '))
numero2 = int(input('Ingresa el segundo numero: '))

if numero1%numero2 == 0:
    print(f'El numero {numero1} es multiplo del numero {numero2}')
elif numero2%numero1 == 0:
    print(f'El numero {numero2} es multiplo del numero {numero1}')
else:
    print('Ninguno de los numeros ingresados es multiplo del otro')

print()

print('-'*20,'MULTIPLOS - UN NUMERO','-'*20)

def esMultiplo(numero1,numero2):
    if numero1%numero2 == 0:
        print(f'El numero {numero1} es multiplo del numero {numero2}')
    else:
        print(f'El numero {numero1} no es multiplo del numero {numero2}')
        
esMultiplo(numero1,numero2)