'''Solicite al usuario un cantidad numerica que expresa segundos
(medida de tiempo). Expresela (conviertala) en horas minutos y segundos.
Segund el caso'''

segundos_h=int(input("Segundos a horas: "))
hora=segundos_h//3600
minutos=segundos_h//60
segundos=segundos_h//1

print("Son: ", hora, "horas.", "Son:", minutos, "minutos.", "Son:", segundos,"segundos.")