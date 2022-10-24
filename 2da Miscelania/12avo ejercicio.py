'''Solicitela hora en formato horas, minutos y segundos. Imprima
en pantalla la hora que sera dentro de 1 segundo'''

hora=int(input("Ingresa la hora: "))
minutos=int(input("Ingresa los minutos: "))
segundos=int(input("Ingresa los segundos: "))

hora1=hora+1
minutos1=00
segundos1=00
minutos2=minutos+1
hora_final=segundos+1
if hora_final<60:
    print( "La hora final +1segundo es: ",hora, ":", minutos,":", hora_final)
elif segundos>=59 and minutos>=59:
    print("La hora final +1segundo es: ",hora1,":", minutos1, ":", segundos1)
elif segundos>=59:
    print("La hora final +1segundo es:",hora, ":", minutos2, ":", segundos1 )  
  