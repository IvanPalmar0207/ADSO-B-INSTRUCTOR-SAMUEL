'''-Imprima todas las subcadenas que salen de una cadena comenzando con 
las dos primeras letras, luego tres primeras y así sucesivamente hasta 
llegar a la última
'''
def subcadenas(strr): 
    s=1
    for i in strr:
        s+=1
        print(strr[0:s])
#Esto es una ejecucion de ejemplo:)
ejemplo=input('¿Cual es tu palabra?\n-')
subcadenas(ejemplo)
