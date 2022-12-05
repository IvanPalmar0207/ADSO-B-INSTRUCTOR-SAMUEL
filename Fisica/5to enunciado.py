'''Crea una funcion que calcule la energia cinetica de 
un automovil de masa de(numero ingresado por el usuario)Kg 
que se dirige hacia Ibague a una velocidad de (numero 
ingresado por el usuario) Km/h'''
def energia_cinetica(velocidad,masa):
    velocidad_final=velocidad*1000/3600
    ec=1/2*masa*(velocidad_final)**2
    print(f'La energia cinetica que alcanza el automovil es {ec} J')
    
velocidad=float(input('¿A que velocidad anda el vehiculo?(Km/h) '))
masa=float(input('¿Cual es la masa del vehiculo?(Kg) '))
energia_cinetica(velocidad,masa)