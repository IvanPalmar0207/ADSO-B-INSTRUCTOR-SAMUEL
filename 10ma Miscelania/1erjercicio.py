'''-Cuantas letras del abecedario estan en la cadena, si estan repetidas 
cuentela solo una vez'''
def repetidas(string):
    abecedario='abcdefghijklmnñopqrstuvwxyzáéíóúÁÉÍÓÚABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    lista=[]
    rep=[]
    c1=0
    for i in string:
        if i in abecedario:
            lista.append(i)
    for j in lista:
        if j not in rep and j in abecedario:
            c1+=1
            rep.append(j)
    print('El total de letras es',c1)
    print(rep)  
#Esto es un ejemplo:)
ejemplo=input('¿Cual es tu palabra?\n-')         
repetidas(ejemplo)