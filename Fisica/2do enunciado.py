'''Crea una funcion que diga el trabajo que realiza una
grua al elevar un bloque de (numero ingresado por el usuario)
KG a una altura de (numero ingresado por el usuario) metros'''
def grua(masa,altura):
    gravedad=9.8
    trabajo=masa*gravedad*altura
    final=round(trabajo,2)
    print(f'El trabajo que realizo la grua al elevar el bloque fue de {final} J')
masa=float(input('¿Cual es el peso del bloque (KG)? '))
altura=float(input('¿A que altura se elevara el bloque (metros)? '))
grua(masa,altura)