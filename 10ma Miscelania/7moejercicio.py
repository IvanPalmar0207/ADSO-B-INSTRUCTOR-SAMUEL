'''-De una cadena diga cuantas vocales tiene, cuantas consonantes, 
cuantas vocales con tilde y cuantos caracteres especiales.
'''
def tildes(strr):
    p1='aeiouAEIOU'
    p2='bcdfghjklmnñopqrstvwxyzBCDFGHJKLMNÑOPQRSTUVWXYZ'
    p3='áéíóúÁÉÍÓÚ'
    c=0
    c1=0
    c2=0
    c3=0
    for i in strr:
        if i in p1:
            c+=1
        elif i in p3:
            c3+=1
        elif i in p2:
            c1+=1
        elif i != p1 and i != p2 and i !=p3:
            c2+=1
    print('El numero de vocales sin tilde que tiene la cadena son:',c)
    print('El numero de vocales con tilde que tiene la cadena son:',c3)
    print('El numero de consonantes que tiene la cadena son:',c1)
    print('El numero de caracteres especiales que tiene la cadena son:',c2)
#Esto es un ejemplo de ejecucion:)
ejemplo=input('¿Cual es tu cadena?\n-')
tildes(ejemplo)