def promedio(lista):
    s=0
    p=0
    for i in lista:
        s+=1
        p+=i
        total=p/s
    print('Los numeros de tu lista son',lista)
    print('El promedio de tu lista es',total)

def sumar(lista):
    s=0
    for i in lista:
        s+=i
    return s

def resta(lista):
    s=0
    for i in lista:
        s-=i
    return s

def par_smpr(lista):
    print('!Esta funcion te sirve para hallar el promedio de los numeros pares de una lista¡')
    suma=0
    par1=0
    par=[]
    for i in lista:
        if i%2==0:
            suma+=1
            par1+=i
            promedio=par1/suma
            par.append(i)
    print('\nEl contenido de tu lista es',lista)
    print('Los numeros pares de tu lista son:',par)
    print('El promedio de tu lista es',promedio)

def impar_smpr(lista):
    print('!Esta funcion te sirve para hallar el promedio de los numeros impares de una lista¡')
    suma=0
    impar1=0
    impar=[]
    for i in lista:
        if i%2!=0:
            suma+=1
            impar1+=i
            promedio=impar1/suma
            impar.append(i)
    print('\nEl contenido de tu lista es',lista)
    print('Los numero impares de tu lista son:',impar)
    print('El promedio de tu lista es',promedio)

def full_list(lista):
    import random
    print('!Esta funcion te sirve para llenar una lista de numeros aleatorios, los que tu escogas¡')
    numeros=int(input('¿Cual es el primer(inicio) numero para el rango de numeros aleatorios que deseas?\n-'))
    numeros2=int(input('¿Cual es el segundo(fin) numero para el rango de numeros aleatorios que deseas?\n-'))
    n1=int(input('¿Desde donde quieres que empiece tu lista?\n-'))
    n2=int(input('¿Hasta donde quieres que vaya tu lista?\n-'))
    lista=[(random.randint(numeros,numeros2)) for i in range(n1,n2+1)]
    print('Tu lista de numeros aleatorios es:',lista)

def palindromo(lista):

    print('!Esta funcion te ayudara a identificar las palabras palindromas de tu lista¡')
    vacia=[]
    for i in lista:
        log=len(i)
        a=i[log::-1]
        if i==a:
            vacia.append(i)
            print(i,'es una palabra palindroma')
        else:
            print(i,'no es una palabra palindroma')
    print('Las palabras palindromas son:',vacia)            

def agregar(lista):
    print('!Esta funcion te permite agregar contenido(strings) a tu lista¡')
    while True:
        palabra=input('¿Que palabra deseas agregar?\n-')
        if palabra=='Salir' or palabra=='salir':
            break
        elif palabra not in lista:
            lista.append(palabra)
        elif palabra in lista:
            continue
    print(lista)

def eliminar(lista):
    palabra=int(input('¿Que indice deseas eliminar?(Desde el indice 0 a-1)\n-'))
    for i in lista:
        indice=lista.index(i)
        if palabra==indice:
            lista.pop(palabra)
    print(lista)