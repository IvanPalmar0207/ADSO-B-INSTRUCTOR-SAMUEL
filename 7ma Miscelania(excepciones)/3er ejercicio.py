''' Hacer una lista co los dias de la semana pero si se ingresa un numero
diferente a 6 votara un error (funcion)'''

def semanas():
    try:
        print('Ingresa un numero de 0 a 6 y tu dia elegido aparecera(Lunes, Martes, etc)')
        dias=int(input('¿Que numero deseas seleccionar? '))
        semana=['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
        for i in semana[dias]:
            print(i, end='')
        print('\nGracias por elegir un numero')
    except IndexError:
        print('El numero no se encuentra en el rango establecido')
        print('Gracias por elegir un numero igualmente')
    except:
        print('Otro error aparte del de rango ha sido reconocido')
        print('Gracias por elegir un numero igualmente')
semanas()