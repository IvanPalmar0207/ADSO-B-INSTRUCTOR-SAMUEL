''' Solicite un angulo al usuario en grados. Diga en que cuadrante esta.
Diga ademas en que vuelta esta sabiendo que 360 grados se completa una vuelta
a la circunferencia. Ademas diga el resultado en radianes'''

angulo=float(input("Digita tu angulo: "))

if angulo>0 and angulo<90:
    print ('cuadrante I')
elif angulo>90 and angulo<180:
    print ('cuadrante II')
elif angulo>180 and angulo<270:
    print ('cuadrante III')
elif angulo>270 and angulo<360:
    print ('cuadrante IV')
elif angulo==0 or angulo==180 or angulo==360:
    print ('Eje X')
elif angulo==90 or angulo==270:
    print ('Eje Y')

if angulo < 360:
    print("No cuenta con vueltas")
elif angulo==360:
    print("Equivale a 1 vuelta")
elif angulo > 360 and angulo <= 720:
    print("Equivale a 2 vueltas")
elif angulo > 720 and angulo <= 1080:
    print("Equivale a 3 vueltas")
elif angulo > 1080 and angulo <= 1440:
    print("Equivale a 4 vueltas")
elif angulo > 1440 and angulo <= 1800:
    print("Equivale a 5 vueltas")
elif angulo > 1800 and angulo <= 2160:
    print("Equivale a 6 vueltas")   
elif angulo > 2160 and angulo <= 2520:
    print("Equivale a 7 vueltas")
elif angulo > 2520 and angulo <= 2880:
    print("Equivale a 8 vueltas")
elif angulo > 2880 and angulo <= 3240:
    print("Equivale a 9 vueltas")
elif angulo > 3240 and angulo <= 3600:
    print("Equivale a 10 vueltas")
elif angulo > 3600 and angulo <= 3960:
    print("Equivale a 11 vueltas")
elif angulo > 3960 and angulo <= 4320:
    print("Equivale a 12 vueltas")
elif angulo > 4320 and angulo <= 4680:
    print("Equivale a 13 vueltas")
elif angulo > 4680 and angulo <= 5040:
    print("Equivale a 14 vueltas")
elif angulo > 5040 and angulo <= 5400:
    print("Equivale a 15 vueltas")
elif angulo > 5400 and angulo <= 5760:
    print("Equivale a 16 vueltas")
elif angulo > 5760 and angulo <= 6120:
    print("Equivale a 17 vueltas")
elif angulo > 6120 and angulo <= 6480:
    print("Equivale a 18 vueltas")
elif angulo > 6480 and angulo <= 6840:
    print("Equivale a 19 vueltas")
elif angulo > 6840 and angulo <= 7200:
    print("Equivale a 20 vueltas")
else:
    print("El angulo es demasiado grande")    

radianes=angulo*3.14/180
print("El resultado en radianes es: ", radianes)

