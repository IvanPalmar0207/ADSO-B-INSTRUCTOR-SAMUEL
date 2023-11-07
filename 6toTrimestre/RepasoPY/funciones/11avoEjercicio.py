'''
El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido 
desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos 
diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:

LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).
DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
EsBisiesto: Recibe un año y nos dice si es bisiesto.
Calcular_Dia_Juliano: recibe una fecha y nos devuelve el día juliano.
'''

import datetime

def leerFecha(año,mes,dia):
    leerFecha = datetime.date(año,mes,dia)
    return leerFecha

def diasDelMes(año,mes):    
    mes31 = 31
    mes30 = 30
    mes28 = 28
    mes29 = 29
    
    if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print(f'El mes {mes} en el año {año} tiene {mes31} dias')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print(f'El mes {mes} en el año {año} tiene {mes30} dias')
        elif mes == 2:
            print(f'El mes {mes} en el año {año} tiene {mes29} dias')
    else:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print(f'El mes {mes} en el año {año} tiene {mes31} dias')
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            print(f'El mes {mes} en el año {año} tiene {mes30} dias')
        elif mes == 2:
            print(f'El mes {mes} en el año {año} tiene {mes28} dias')    

def esBisiesto(año):
    if año % 4 == 0 and (año % 400 == 0 or año % 100 != 0):
        print(f'El año {año} es bisiesto')
    else:
        print(f'El año {año} no es bisiesto')
    
def calcularDiaJuliano(año,mes,dia):
    a = (14 - mes) // 12
    y = año + 4800 - a
    m = mes + 12 * a - 3
    diaJuliano = dia + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 3204
    return diaJuliano


def menu():
    while True:
        print('-'*20,'FECHAS Y SUS CONVERSIONES','-'*20)
        print()
        print('1. Leer una fecha, ingresar año, mes y dia')
        print('2. Calcular los dias del mes, dar una año y un mes')
        print('3. Calcular un año bisiesto, ingresar un año')
        print('4. Calcular el dia juliano, ingresar un año, mes y un dia')
        print('0. Salir del sistema')
        print()
        opcion = int(input('Que accion deseas hacer?\n-'))
        print()
        
        match opcion:
            case 1:
                print('-'*10,'LEER FECHAS','-'*10)
                año = int(input('Ingresa el año: '))
                mes = int(input('Ingresa el mes: '))
                dia = int(input('Ingresa el dia: '))
                print(f'La fecha que ingresaste es {leerFecha(año,mes,dia)}') 
                print()
                resultado = input('Deseas volver?\n-')
            
                if resultado.upper() == 'NO':
                    print()
                    año = int(input('Ingresa el año: '))
                    mes = int(input('Ingresa el mes: '))
                    dia = int(input('Ingresa el dia: '))
                    print()
                    print(f'La fecha que ingresaste es {leerFecha(año,mes,dia)}') 
                else:
                    continue
                    
            case 2:
                print('-'*10,'CALCULAR DIAS DE UN MES','-'*10)            
                año = int(input('Ingresa el año: '))
                mes = int(input('Ingresa el mes: '))
                diasDelMes(año,mes)
                print()
                resultado = input('Deseas volver?\n-')
                
                if resultado.upper() == 'NO':
                    año = int(input('Ingresa el año: '))
                    mes = int(input('Ingresa el mes: '))
                    diasDelMes(año,mes)
                    print()
                else:
                    continue
                
            case 3:
                print('-'*10,'CALCULAR AÑOS BISIESTOS','-'*10)
                print()
                año = int(input('Ingresa un año: '))
                esBisiesto(año)
                print()
                
                resultado = input('Deseas volver?\n-')
                if resultado.upper() == 'NO':
                    print()
                    año = int(input('Ingresa un año:'))
                    esBisiesto(año)    
                    print()
                else:
                    continue
                
            case 4:
                print('-'*10,'DIA JULIANO','-'*10)
                print()
                año = int(input('Ingresa el año: '))
                mes = int(input('Ingresa el mes: '))
                dia = int(input('Ingresa el dia: '))
                print(f'El dia juliano con la fecha ingresada es {calcularDiaJuliano(año,mes,dia)}')
                print()
                resultado = input('Deseas volver?\n-')
                
                if resultado.upper() == 'NO':
                    print()
                    año = int(input('Ingresa el año: '))
                    mes = int(input('Ingresa el mes: '))
                    dia = int(input('Ingresa el dia: '))
                    print(f'El dia juliano de la fecha ingresada es {calcularDiaJuliano(año,mes,dia)}')
                    print()
                else:
                    continue    
                
            case 0:
                print('Has decidido salir, gracias por usar nuestro sistema de fechas')
                break
    
menu()