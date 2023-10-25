from viruelaSimica import *

#Casos de contagio en Antioquia
print('-'*85)
print('CASOS DE CONTAGIOS EN ANTIOQUIA')
print()
contador = 0
for i in response:
    if i['nom_dep_not'] == 'ANTIOQUIA':
        contador += 1
print('El numero de casos de contagios en el departamento de Antioquia fue de',contador,'personas')
print('-'*85)

