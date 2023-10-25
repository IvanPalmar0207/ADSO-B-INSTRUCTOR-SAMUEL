from viruelaSimica import *

#Numero de mujeres contagiada
print('-'*50)
print('MUJERES CONTAGIADAS')
print()
contador = 0
for i in response:
    for j in i['sexo']:
        if j == 'F':
            contador+=1
print('El numero total de mujeres contagiadas fue: ',contador)
print('-'*50)