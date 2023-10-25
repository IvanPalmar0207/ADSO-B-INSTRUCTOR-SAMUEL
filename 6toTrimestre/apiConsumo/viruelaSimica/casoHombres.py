from viruelaSimica import *

#Numero de hombres contagiados
print('-'*50)
print('HOMBRES CONTAGIADOS')
print()
contador = 0
for i in response:
    for j in i['sexo']:
        if j == 'M':
            contador+=1
print('El numero total de hombres contagiados fue: ',contador)
print('-'*50)