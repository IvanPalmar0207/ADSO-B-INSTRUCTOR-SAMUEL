from viruelaSimica import *

#Numero de hombres contagiados
contador = 0
for i in response:
    for j in i['nom_dep_not']:
        if i['nom_dep_not'] == 'BOGOTA':
            contador += 1
print(contador)        