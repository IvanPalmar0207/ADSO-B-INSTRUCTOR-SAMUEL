from viruelaSimica import *

#Personas contagias menores o de 30 años
print('-'*70)
print('NUMERO DE PERSONAS CONTAGIADAS MENORES O DE 30 AÑOS')
print()
contador = 0
for i in response:
    edad = int(i['edad'])
    if edad <= 30:
        contador += 1
print('El numero de personas menores o de 30 años contagiadas es de:',contador)
print('-'*70)        