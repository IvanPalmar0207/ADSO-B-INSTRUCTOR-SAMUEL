'''Crea una funcion que pueda calcular 
el trabajo que puede realizar en una hora un motor 
de (numero ingresado por el usuario) CV'''
def trabajo_motor(motor):
    watts=735
    potencia=motor*watts
    tiempo=3600
    trabajo=potencia*tiempo
    print('El trabajo realizado por el moto es de ',trabajo,'J en una hora') 
motor=float(input('¿Cual es la potencia del motor?' ))
trabajo_motor(motor)