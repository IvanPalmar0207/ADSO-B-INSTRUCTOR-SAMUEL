from viruelaSimica import * 

#Contagios por estrato
print('-'*40)
print('NUMERO DE CONTAGIOS DE LOS 6 ESTRATOS')
print()
estrato1 = 0
estrato2 = 0
estrato3 = 0
estrato4 = 0
estrato5 = 0
estrato6 = 0
masEstratos = 0

for i in response:
    estrato = i['estrato']
    if estrato == '1':
        estrato1 += 1    
    
    elif estrato == '2':
        estrato2 += 1        
    
    elif estrato == '3':
        estrato3 += 1        
    
    elif estrato == '4':
        estrato4 += 1    
    
    elif estrato == '5':
        estrato5 += 1                 
    
    elif estrato == '6':
        estrato6 += 1                
    
    else:
        masEstratos+=1        
 
suma = (estrato1+estrato2+estrato3+estrato4+estrato5+estrato6+masEstratos)
#Visualizacion del total de contagiados       
print('El estrato 1 tuvo',estrato1,'contagiados\n')
print('El estrato 2 tuvo',estrato2,'contagiados\n')
print('El estrato 3 tuvo',estrato3,'contagiados\n')
print('El estrato 4 tuvo',estrato4,'contagiados\n')
print('El estrato 5 tuvo',estrato5,'contagiados\n')
print('El estrato 6 tuvo',estrato6,'contagiados\n')
print('Los demas estratos tuvieron',masEstratos,'contagiados\n')
print('El numero total de contagiados fue de',suma,'personas\n')
print('-'*40)