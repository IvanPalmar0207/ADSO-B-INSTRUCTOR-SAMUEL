'''
Escribir dos funciones que permitan calcular:

La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú donde se pueda elegir la opción de convertir
a segundos, convertir a horas,minutos y segundos o salir del programa.
'''

def conversionHorasMinutos(horas,minutos,segundos):
    horas = horas * 3600
    minutos = minutos * 60
    segundos = segundos
    print(f'Las horas en segundos equivalen a: {horas} segundos\nLos minutos a segundos equivalen a: {minutos} segundos\nLos segundos equivalen a: {segundos} segundos')

def conversionSegundos(segundos):
    hora = segundos / 3600
    minutos = segundos / 60
    segundos = segundos
    
    print(f'Los segundos en horas equivalen a: {round(hora,2)} horas\nLos segundos en minutos equivalen a: {round(minutos,2)} minutos\nLos segundos equivalen a: {segundos} segundos')    
    
    
def menu():
    while True:
        print('-'*20,'CONVERSIONES DE TIEMPO','-'*20)
        print('1. Convertir de segundos a horas, minutos y segundos')
        print('2. Convertir de horas, minutos y segundos a segundos') 
        print('0. Salir\n')
        opcion = int(input('Cual accion deseas realizar?\n-'))
        match opcion:
            case 1:
                segundos = int(input('Ingresa una cantidad en segundos: '))
                conversionSegundos(segundos)
                print()
                resultado = input('Deseas volver?\n-')
                if resultado.upper() == 'NO':
                    print()
                    segundos = int(input('Ingresa una cantidad en segundos: '))
                    conversionSegundos()         
                else:
                    continue
            case 2:
                horas = int(input('Ingresa las horas: '))
                minutos = int(input('Ingresa los minutos: '))
                segundos = int(input('Ingresa los segundos:'))
                print()
                conversionHorasMinutos(horas,minutos,segundos)
                print()
                resultado = input('Deseas volver?\n-')
                if resultado.upper() == 'NO':
                    horas = int(input('Ingresa las horas: '))
                    minutos = int(input('Ingresa los minutos: '))
                    segundos = int(input('Ingresa los segundos:'))
                    conversionHorasMinutos(horas,minutos,segundos)
                else:
                    continue
            case 0:
                print('Gracias por usar nuestro sistema de conversion')
                break      
            
menu()