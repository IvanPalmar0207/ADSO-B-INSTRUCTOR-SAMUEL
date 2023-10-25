from viruelaSimica import *

#Personas mayores a 30 años
print('-'*65)
print('NUMERO DE PERSONAS MAYORES A 30 AÑOS')
print()
contador = 0
for i in response:
    edad = int(i['edad'])
    if edad > 30:
        contador += 1
print('El numero de personas contagiadas mayores a 30 años fue de',contador)    
print('-'*65)