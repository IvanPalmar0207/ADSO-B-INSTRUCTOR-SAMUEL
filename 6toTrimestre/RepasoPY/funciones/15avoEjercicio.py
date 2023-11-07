'''
Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura 
de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el primer
elemento que se añade al conjunto es el primero que se puede sacar.

En realidad nos sirven todas las funciones del ejercicio anterior menos la función SacarDeLaCola que es 
la que tienes que modificar.
'''

def filaLongitud(fila):
    longitud = len(fila)
    return longitud

def filaVacia(fila):
    longitud = len(fila)
    if longitud == 0:
        print('La fila esta vacia')
    else:
        print('La fila cuenta con elementos')
        
def filaLlena(fila):
    longitud = len(fila)
    if longitud == 10:
        print('La fila esta llena')
    else:
        print('La fila esta vacia o le falta elementos para estar llena')
        
def filaAgregar(fila,cadena):
    longitud = len(fila)
    if longitud<10:
        fila.append(cadena)
        print('El elemento ha sido correctamente agregado a la fila')
    else:
        print('La fila esta llena, lo sentimos no se pueden agregar mas elementos')
    
def filaEliminar(fila):
    longitud = len(fila)
    if longitud == 0:
        print('No se pueden eliminar elementos, la pila esta vacia')
    else:
        print('El primer elemento de la fila es: ',fila[0])
        fila.pop(0)
        print('\nEl elemento ha sido eliminado correctamente')
        
def filaEscribir(fila):
    return fila

def menu():
    fila = []
    while True:
        print('-'*20,'PROCESOS CON UNA FILA','-'*20)
        print()
        print('1. Agregar elementos a la fila (Recomendado)')
        print('2. Longitud de la fila')
        print('3. Revisar si la fila esta vacia')
        print('4. Revisar si la fila esta llena')
        print('5. Eliminar el ultimo elemento de la fila')
        print('6. Ver los elementos de la fila')
        print('0. Salir')
        
        opcion = int(input('Que accion deseas realizar?\n-'))
        print()
        
        match opcion:
            case 1:
                print('-'*10,'AGREGAR A LA FILA','-'*10)
                print()
                cadena = input('Ingresa la cadena que vas a agregar: ')
                print()
                filaAgregar(fila,cadena)
                print()
                
                resultado = input('Deseas agregar otro elemento?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    cadena1 = input('Ingresa la cadena que vas a agregar: ')
                    print()
                    filaAgregar(fila,cadena1)
                    print()
                else:
                    continue
                
            case 2:
                print('-'*10,'LONGITUD DE LA FILA','-'*10)
                print()
                print(f'La longitud de la fila es igual a {filaLongitud(fila)}')
                print()                
                resultado = input('Deseas ver de nuevo la longitud?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    print(f'La longitud de la fila es igual a {filaLongitud(fila)}')
                    print()   
                else:
                    continue        
                
            case 3:
                print('-'*10,'LA FILA ESTA VACIA?','-'*10)
                print()
                filaVacia(fila)
                print()                
                resultado = input('Deseas ver de nuevo si la fila esta vacia?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    filaVacia(fila)
                    print()   
                else:
                    continue    
                
            case 4:
                print('-'*10,'LA FILA ESTA LLENA?','-'*10)
                print()
                filaLlena(fila)
                print()                
                resultado = input('Deseas ver de nuevo si la pila esta llena?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    filaLlena(fila)
                    print()   
                else:
                    continue                        
                
            case 5:
                print('-'*10,'ELIMINAR ELEMENTO DE LA FILA','-'*10)
                print()
                filaEliminar(fila)
                print()                
                resultado = input('Deseas eliminar de nuevo el ultimo elemento?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    filaEliminar(fila)
                    print()   
                else:
                    continue                                             
                
            case 6:
                print('-'*10,'ELEMENTOS DE LA FILA','-'*10)
                print()
                print(f'Los elementos de la fila son: {filaEscribir(fila)}')
                print()                
                resultado = input('Deseas ver de nuevo los elementos de la fila?\n- ')
                if resultado.upper() == 'SI':
                    print()
                    print(f'Los elementos de la pila son: {filaEscribir(fila)}')
                    print()   
                else:
                    continue                             
                
            case 0:
                print('Gracias por realizar hacer acciones con una fila, vuelve pronto')
                break
            
menu()