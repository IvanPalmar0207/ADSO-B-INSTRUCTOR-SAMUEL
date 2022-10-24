'''Solicite una fecha al usuario en formato dia, mes y año.
Digale cuanto tiempo ha pasado desde esa fecha hasta hoy o cuanto
falta pra llegar a esa fecha si es posterior'''

from datetime import date
import datetime

año=int(input("Ingresa el año: "))
mes=int(input("Ingresa el mes: "))
dia=int(input("Ingresa el dia: "))

hoy=date.today()
            #Año,mes,dia 
fecha_hoy=date(año,mes,dia)

fecha_final=hoy-fecha_hoy 
fecha_final1=fecha_hoy-hoy
if hoy > fecha_hoy:
    print("Esta fecha fue hace", fecha_final)
elif hoy<fecha_hoy:
    print("Faltan:", fecha_final1 ,"para esta fecha")  
else:
    print("La fecha indicada no puede ser verificada")    
