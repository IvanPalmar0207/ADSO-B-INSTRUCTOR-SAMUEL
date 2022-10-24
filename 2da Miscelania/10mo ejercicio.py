'''Solicite al usuario la hora en formato hh::mm::ss
(hora militar, 24 horas). El prgrama debe responder 
que hora sera un segundo despues. Ej:ingreso 11:59:59,
el programa responde 12::00:00'''

hh=int(input("Ingresar la hora: "))
mm=int(input("Ingresa los mintos: "))
ss=int(input("Ingresa los segundos: "))
hh1=hh+1
mm1=00
ss1=00
mm2=mm+1
hora_final=ss+1
if hora_final<60:
    print( hh, ":", mm,":", hora_final)
elif ss>=59 and mm>=59:
    print(hh1,":", mm1, ":", ss1)
elif ss>=59:
    print(hh, ":", mm2, ":", ss1 )    
    