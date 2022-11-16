'''Pedir una nota de 0 a 10 y mostrarla de la forma:
insuficiente, suficiente, bien, etc. Use la escala que
prefiera, pero cerciorese que tiene 5 valores'''

def nota(nota=float(input("Ingresa la nota: "))):
    if nota < 0:
        return "No aplica"
    elif nota <= 2:
        return "INSUFICIENTE"
    elif nota<= 6:
        return "BAJO"
    elif nota<= 7.5:
        return "BASICO"
    elif nota <= 8.9:
        return "ALTO"
    elif nota <= 10:
        return "SUPERIOR"
    else:
        return "No tiene calificacion"
    
print(nota())