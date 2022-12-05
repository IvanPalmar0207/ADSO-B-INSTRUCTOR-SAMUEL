'''Crea una funcion que calcule el trabajo realizado por un
motor de (numero ingresado por el usuario)Cv en 10 minutos
y calcular su potencia en vatios y kilovatios'''
def vatios_kilovatios(motor):
    vatios=motor*735
    kilovatios=vatios*1/1000
    minutos=10*60
    trabajo=vatios*minutos
    print(f'''La potencia del motor en vatios es {vatios} W y en kilovatios es {kilovatios} KW,
el trabajo que realizo en 10 minutos es {trabajo} J''')

motor=int(input('¿Cual es la potencia del motor? '))
vatios_kilovatios(motor)
