'''Pedir una nota de 0 a 10 y mostrarla de la forma:
insuficiente, suficiente, bien, etc. Use la escala que
prefiera, pero cerciorese que tiene 5 valores'''

nota=float(input("Ingresa la nota: "))
if nota <= 2:
    print("INSUFICIENTE")
elif nota<= 6:
    print("BAJO")     
elif nota<= 7.5:
    print("BASICO")
elif nota <= 8.9:
    print("ALTO")
elif nota <= 10:
    print("SUPERIOR")   
else:
    print("No tiene calificacion")         