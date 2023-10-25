from viruelaSimica import *

#Casos de contagiados en Bogota
print('-'*70)
print('CASOS DE CONTAGIOS EN BOGOTA')
print()
contador = 0
for i in response: 
    if i['nom_dep_not'] == 'BOGOTA':
        contador += 1        
print('El numero de casos de viruela simica en Bogota fue de',contador,'personas')
print('-'*70)