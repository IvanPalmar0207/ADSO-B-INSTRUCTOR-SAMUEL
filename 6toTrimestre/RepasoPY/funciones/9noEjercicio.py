'''
Crear una función que calcule el MCD de dos número por el método de Euclides. El método de Euclides es 
el siguiente:

Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre el resto obtenido y 
se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD.
'''

def metodoEuclides(numero1,numero2):
    if numero1 > numero2:
        while True:
            residuo = numero1 % numero2
            if residuo == 0:
                print(f'El mcd es igual a {numero2}')
                break
            else:
                numero1 = numero2
                numero2 = residuo                                       
    elif numero2 > numero1:
        while True:
            residuo = numero2 % numero1
            if residuo == 0:
                print(f'El mcd es igual a {numero1}')
                break
            else:
                numero2 = numero1
                numero1 = residuo
        
print('-'*20,'METODO EUCLIDES','-'*20)
print()
numero1 = int(input('Ingresa el primer numero: '))
numero2 = int(input('Ingresa el segundo numero: '))
print()
metodoEuclides(numero1,numero2)