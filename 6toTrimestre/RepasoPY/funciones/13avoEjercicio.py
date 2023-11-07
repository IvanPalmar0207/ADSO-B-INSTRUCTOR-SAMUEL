'''
Queremos crear un programa que trabaje con fracciones a/b. Para  representar una fracción vamos a utilizar dos enteros: numerador y 
denominador. Vamos a crear las siguientes funciones para trabajar con funciones:

Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción. Si el dominador es 1, se muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y dominador por el MCD del numerador y
denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones
es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2.Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la 
fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. Se debe 
simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. Se debe 
simplificar la fracción resultado.

Crear un programa que utilizando las funciones anteriores muestre
el siguiente menú:

Sumar dos fracciones: En esta opción se piden dos fracciones y se 
muestra el resultado.
Restar dos fracciones: En esta opción se piden dos fracciones y se
muestra la resta.
Multiplicar dos fracciones: En esta opción se piden dos fracciones y 
se muestra la producto.
Dividir dos fracciones: En esta opción se piden dos fracciones y
se muestra la cociente.
Salir
'''

def simplificarFraccion(numerador1,denominador1):   
    while True:
        residuo = numerador1 % denominador1
        if residuo == 0:
            resultado = denominador1
            break        
        else:
            numerador1 = denominador1
            denominador1 = residuo
    print(f'La fraccion simplificada es igual a: {denominador1}')
    
def leerFraccion(numerador,denominador):
    print(f'La fraccion es:\n {numerador}\n---\n {denominador}')
    simplificarFraccion(numerador,denominador)
   
def escribirFraccion(numerador,denominador):
    if denominador<=1:
        print(f'La fraccion es: {numerador}')
        simplificarFraccion(numerador,denominador)
    else: 
        print(f'La fraccion es:\n {numerador}\n---\n {denominador}')
        simplificarFraccion(numerador,denominador)

def sumarFracciones(numerador1,denominador1,numerador2,denominador2):
    print(f'La primera fraccion es:\n {numerador1}\n---\n {denominador1}')
    print(f'La segunda fraccion es:\n {numerador2}\n---\n {denominador2}')
    numeradorResultado = (numerador1 * denominador2) + (denominador1 * numerador2)
    denominadorResultado = denominador1 * denominador2
    print(f'\nEl resultado de la suma sin simplificar es:\n {numeradorResultado}\n---\n {denominadorResultado}')
    print()
    simplificarFraccion(numeradorResultado,denominadorResultado)
    
def restarFracciones(numerador1,denominador1,numerador2,denominador2):
    if denominador1 == denominador2:
        print(f'La primera fraccion es:\n {numerador1}\n---\n {denominador1}')
        print(f'La segunda fraccion es:\n {numerador2}\n---\n {denominador2}')
        numeradorResultado = numerador1 - numerador2
        print(f'\nEl resultado de la resta sin simplificar es:\n {numeradorResultado}\n---\n {denominador1}')
        print()
        simplificarFraccion(numeradorResultado,denominador1)
    else:
        print(f'La primera fraccion es:\n {numerador1}\n---\n {denominador1}')
        print(f'La segunda fraccion es:\n {numerador2}\n---\n {denominador2}')
        numeradorResultado = (numerador1 * denominador2) - (numerador2 * denominador1)
        denominadorResultado = denominador1 * denominador2
        print(f'\nEl resultado de la resta sin simplificar es:\n {numeradorResultado}\n---\n {denominadorResultado}')
        print()
        simplificarFraccion(numeradorResultado,denominadorResultado)
    
def multiplicarFraccion(numerador1,denominador1,numerador2,denominador2):
    print(f'La primera fraccion es:\n {numerador1}\n---\n {denominador1}')
    print(f'La segunda fraccion es:\n {numerador2}\n---\n {denominador2}')
    numeradorResultado = numerador1 * numerador2
    denominadorResultado = denominador1 * denominador2
    print(f'\nEl resultado de la multiplicacion sin simplificar es:\n {numeradorResultado}\n---\n {denominadorResultado}')
    print()
    simplificarFraccion(numeradorResultado,denominadorResultado)

def dividirFracciones(numerador1,denominador1,numerador2,denominador2):
    print(f'La primera fraccion es:\n {numerador1}\n---\n {denominador1}')
    print(f'La segunda fraccion es:\n {numerador2}\n---\n {denominador2}')
    numeradorResultado = numerador1 * denominador2
    denominadorResultado = denominador1 * numerador2
    print(f'\nEl resultado de la division sin simplificar es:\n {numeradorResultado}\n---\n {denominadorResultado}')
    print()
    simplificarFraccion(numeradorResultado,denominadorResultado)

def menu():
    while True:
        print('-'*20,'OPERACIONES CON FRACIONES','-'*20)
        print()
        print('1. Sumar fracciones')
        print('2. Restar fracciones')
        print('3. Multiplicar fracciones')
        print('4. Dividir fracciones')
        print('5. Simplificar fraccion')
        print('6. Leer fraccion')
        print('7. Escribir Fraccion')
        print('0. Salir')
        print()
        opcion = int(input('Que operacion vas a realizar?\n- '))
        
        match opcion:
            case 1:
                print('\n','-'*10,'SUMA DE FRACCIONES','-'*10,'\n')
                print('Primera Fraccion')
                numerador1 = int(input('Ingresa el numerador: '))
                denominador1 = int(input('Ingresa el denominador: '))
                print()                
                print('Segunda Fraccion')                
                numerador2 = int(input('Ingresa el numerador: '))
                denominador2 = int(input('Ingresa el denominador: '))
                print()            
                sumarFracciones(numerador1,denominador1,numerador2,denominador2)
                print()

                resultado = input('Deseas volver?\n- ')
                if resultado.upper() == 'NO':
                    print()
                    print('Primera Fraccion')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))
                    print()
                    print('Segunda Fraccion')
                    numerador2 = int(input('Ingresa el numerador: '))
                    denominador2 = int(input('Ingresa el denominador: '))
                    print()            
                    sumarFracciones(numerador1,denominador1,numerador2,denominador2)
                    print()
                else:
                    continue
                
            case 2:
                print('\n','-'*10,'RESTA DE FRACCIONES','-'*10,'\n')
                print('Primera Fraccion')
                numerador1 = int(input('Ingresa el numerador: '))
                denominador1 = int(input('Ingresa el denominador: '))
                print()                
                print('Segunda Fraccion')                
                numerador2 = int(input('Ingresa el numerador: '))
                denominador2 = int(input('Ingresa el denominador: '))
                print()            
                restarFracciones(numerador1,denominador1,numerador2,denominador2)
                print()

                resultado = input('Deseas volver?\n- ')
                if resultado.upper() == 'NO':
                    print()
                    print('Primera Fraccion')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))
                    print()
                    print('Segunda Fraccion')
                    numerador2 = int(input('Ingresa el numerador: '))
                    denominador2 = int(input('Ingresa el denominador: '))
                    print()            
                    restarFracciones(numerador1,denominador1,numerador2,denominador2)
                    print()
                else:
                    continue

            case 3:
                print('\n','-'*10,'MULTIPLICAR DE FRACCIONES','-'*10,'\n')
                print('Primera Fraccion')
                numerador1 = int(input('Ingresa el numerador: '))
                denominador1 = int(input('Ingresa el denominador: '))
                print()                
                print('Segunda Fraccion')                
                numerador2 = int(input('Ingresa el numerador: '))
                denominador2 = int(input('Ingresa el denominador: '))
                print()            
                multiplicarFraccion(numerador1,denominador1,numerador2,denominador2)
                print()

                resultado = input('Deseas volver?\n- ')
                if resultado.upper() == 'NO':
                    print()
                    print('Primera Fraccion')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))
                    print()
                    print('Segunda Fraccion')
                    numerador2 = int(input('Ingresa el numerador: '))
                    denominador2 = int(input('Ingresa el denominador: '))
                    print()            
                    multiplicarFraccion(numerador1,denominador1,numerador2,denominador2)
                    print()
                else:
                    continue
                    
            case 4:
                    print('\n','-'*10,'DIVISION DE FRACCIONES','-'*10,'\n')
                    print('Primera Fraccion')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))
                    print()                
                    print('Segunda Fraccion')                
                    numerador2 = int(input('Ingresa el numerador: '))
                    denominador2 = int(input('Ingresa el denominador: '))
                    print()            
                    dividirFracciones(numerador1,denominador1,numerador2,denominador2)
                    print()

                    resultado = input('Deseas volver?\n- ')
                    if resultado.upper() == 'NO':
                        print()
                        print('Primera Fraccion')
                        numerador1 = int(input('Ingresa el numerador: '))
                        denominador1 = int(input('Ingresa el denominador: '))
                        print()
                        print('Segunda Fraccion')
                        numerador2 = int(input('Ingresa el numerador: '))
                        denominador2 = int(input('Ingresa el denominador: '))
                        print()            
                        dividirFracciones(numerador1,denominador1,numerador2,denominador2)
                        print()
                    else:
                        continue
                    
            case 5:
                    print('\n','-'*10,'SIMPLIFICAR FRACCION','-'*10,'\n')
                    print('Fraccion a Simplificar')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))                    
                    print()            
                    simplificarFraccion(numerador1,denominador1)
                    print()

                    resultado = input('Deseas volver?\n- ')
                    if resultado.upper() == 'NO':
                        print()
                        print('Fraccion a Simplificar')
                        numerador1 = int(input('Ingresa el numerador: '))
                        denominador1 = int(input('Ingresa el denominador: '))
                        print()            
                        simplificarFraccion(numerador1,denominador1)
                        print()
                    else:
                        continue
                
            case 6:
                    print('\n','-'*10,'LEER FRACCION','-'*10,'\n')
                    print('Fraccion a Leer')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))                    
                    print()            
                    leerFraccion(numerador1,denominador1)
                    print()

                    resultado = input('Deseas volver?\n- ')
                    if resultado.upper() == 'NO':
                        print()
                        print('Fraccion a Leer')
                        numerador1 = int(input('Ingresa el numerador: '))
                        denominador1 = int(input('Ingresa el denominador: '))
                        print()            
                        leerFraccion(numerador1,denominador1)
                        print()
                    else:
                        continue
                    
            case 7:                
                    print('\n','-'*10,'ESCRIBIR FRACCION','-'*10,'\n')
                    print('Fraccion a Escribir')
                    numerador1 = int(input('Ingresa el numerador: '))
                    denominador1 = int(input('Ingresa el denominador: '))                    
                    print()            
                    escribirFraccion(numerador1,denominador1)
                    print()

                    resultado = input('Deseas volver?\n- ')
                    if resultado.upper() == 'NO':
                        print()
                        print('Fraccion a Simplificar')
                        numerador1 = int(input('Ingresa el numerador: '))
                        denominador1 = int(input('Ingresa el denominador: '))
                        print()            
                        escribirFraccion(numerador1,denominador1)
                        print()
                    else:
                        continue                                
                                                            
            case 0:
                print('!Has decidido salir de sistema, gracias por usar nuesro sistema de fracciones¡')
                break

    
menu()