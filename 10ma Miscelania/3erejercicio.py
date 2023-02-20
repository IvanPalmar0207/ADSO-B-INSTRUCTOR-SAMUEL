'''-Cuantas veces se repite un caracter dado'''
def caracter(string):
    x=input('¿Cual es el caracter que deseas buscar?\n-')
    c=0
    for i in string:
        if x in i:
            c+=1
    print(x,'dentro de la palabra \'',string,'\' se repite',c,'veces')
#Esto es un ejemplo de salida:)
ejemplo=input('¿Cual palabra deseas buscar?\n-')
caracter(ejemplo)