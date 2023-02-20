'''- Solicite cadena e imprimala en todas las formas posibles en cuanto 
a mayusculas y minusculas'''
def cadena(str):
    print('Mayusculas:',str.upper())
    print('Minusculas:',str.lower())
    print('Primera letra a mayuscula:',str.capitalize())
    print('Mayusculas por minuscula o viceversa:',str.swapcase())
    print('Titulo:',str.title())
    print('Validacion_mayuscula:',str.isupper())
    print('Validacion_minuscula:',str.islower())
#Esto es un ejemplo de salida:)
ejemplo=input('¿Cual es tu palabra?\n-')
cadena(ejemplo)