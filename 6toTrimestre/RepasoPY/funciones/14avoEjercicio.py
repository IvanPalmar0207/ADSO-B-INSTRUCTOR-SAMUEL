'''
Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.

Para representar una pila vamos a utilizar una lista de cadenas de caracteres.

Vamos a crear varias funciones para trabajar con la pila:

LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena.
si esta llena muestra un mensaje de error.
SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía 
muestra un mensaje de error.
EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.
Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:

Añadir elemento a la pila
Sacar elemento de la pila
Longitud de la pila
Mostrar pila
Salir
'''

def pilaLongitud(pila):
    longitud = len(pila)
    return longitud

def pilaVacia(pila):
    longitud = len(pila)
    if longitud == 0:
        print('La pila esta vacia')
    else:
        print('La pila cuenta con elementos')
        
def pilaLlena(pila):
    longitud = len(pila)
    if longitud == 10:
        print('La pila esta llena')
    else:
        print('La pila esta vacia o le falta elementos para estar llena')
        
def pilaAgregar(pila,cadena):
    longitud = len(pila)
    if longitud<10:
        pila.append(cadena)
        print('El elemento ha sido correctamente agregado a la pila')
    else:
        print('La pila esta llena, lo sentimos no se pueden agregar mas elementos')
    
def pilaEliminar(pila):
    longitud = len(pila)
    if longitud == 0:
        print('No se pueden eliminar elementos, la pila esta vacia')
    else:
        print('El ultimo elemento agregado a la pila es: ',pila[-1])
        pila.pop(-1)
        
def pilaEscribir(pila):
    return pila

def menu():
    pila = []
    while True:
        print('-'*20,'PROCESOS CON UNA PILA','-'*20)
        print()
        print('1. Agregar elementos a la pila (Recomendado)')
        print('2. Longitud de la pila')
        print('3. Revisar si la pila esta vacia')
        print('4. Revisar si la pila esta llena')
        print('5. Eliminar el ultimo elemento de la pila')
        print('6. Ver los elementos de la pila')
        print('0. Salir')
        
        opcion = int(input('Que accion deseas realizar?\n-'))
        print()
        
        match opcion:
            case 1:
                print('-'*10,'AGREGAR A LA PILA','-'*10)
                print()
                cadena = input('Ingresa la cadena que vas a agregar: ')
                print()
                pilaAgregar(pila,cadena)
                print()
                
                resultado = input('Deseas agregar otro elemento?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    cadena1 = input('Ingresa la cadena que vas a agregar: ')
                    print()
                    pilaAgregar(pila,cadena1)
                    print()
                else:
                    continue
                
            case 2:
                print('-'*10,'LONGITUD DE LA PILA','-'*10)
                print()
                print(f'La longitud de la pila es igual a {pilaLongitud(pila)}')
                print()                
                resultado = input('Deseas ver de nuevo la longitud?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    print(f'La longitud de la pila es igual a {pilaLongitud(pila)}')
                    print()   
                else:
                    continue        
                
            case 3:
                print('-'*10,'LA PILA ESTA VACIA?','-'*10)
                print()
                pilaVacia(pila)
                print()                
                resultado = input('Deseas ver de nuevo si la pila esta vacia?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    pilaVacia(pila)
                    print()   
                else:
                    continue    
                
            case 4:
                print('-'*10,'LA PILA ESTA LLENA?','-'*10)
                print()
                pilaLlena(pila)
                print()                
                resultado = input('Deseas ver de nuevo si la pila esta llena?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    pilaLlena(pila)
                    print()   
                else:
                    continue                        
                
            case 5:
                print('-'*10,'ELIMINAR ELEMENTO DE LA PILA','-'*10)
                print()
                pilaEliminar(pila)
                print()                
                resultado = input('Deseas eliminar de nuevo el ultimo elemento?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    pilaEliminar(pila)
                    print()   
                else:
                    continue                                             
                
            case 6:
                print('-'*10,'ELEMENTOS DE LA PILA','-'*10)
                print()
                print(f'Los elementos de la pila son: {pilaEscribir(pila)}')
                print()                
                resultado = input('Deseas ver de nuevo los elementos de la pila?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    print(f'Los elementos de la pila son: {pilaEscribir(pila)}')
                    print()   
                else:
                    continue                             
                
            case 0:
                print('Gracias por realizar hacer acciones con una pila, vuelve pronto')
                break
            
menu()