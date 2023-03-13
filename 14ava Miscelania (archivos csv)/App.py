from Industria import *
import csv

empresas=[]
with open('C:\\Users\\SENA\\Documents\\Ivan_Palmar\\ADSO-B-INSTRUCTOR-SAMUEL\\14ava Miscelania (archivos csv)\\empresas.csv') as flujo:
    leer=csv.reader(flujo)
    for i in leer:
        industrias=industria(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
        empresas.append(industrias)
#print(empresas) Este print identifica si los objetos fueron bien instanciados.
'''for i in empresas:
    print(i.getAll())'''
    


'Analisis de datos'

#Paises
print('Empresas Alrededor del Mundo (Asia y Oceania)')
pais=input('¿De que pais es la empresa que deseas buscar?\n-')
pais1=pais.capitalize()
for i in empresas:
    if pais1 in i.getCountry():
        print(i.getAll())

        

        
#Nombres
print('Empresas en Asia y Oceania')
nombre=input('¿Cual es el nombre de la empresa que deseas buscar?\n-')
nombre1=nombre.capitalize()
for i in empresas:
        if nombre1 in i.getName():
            print(i.getIndex(),i.getOrgaId(),i.getName(),i.getCountry(),i.getNEmplo())
