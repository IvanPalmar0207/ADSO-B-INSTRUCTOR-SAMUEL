'''Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el 
valor numerico de acuerdo a los codigos del alfabeto'''

def codigo(string):
    s=0
    for i in string:
        s+=ord(i)
    return s
#Esto es un ejemplo de salida:)
ejemplo=input('¿Cual es tu palabra?\n-')
print(codigo(ejemplo))