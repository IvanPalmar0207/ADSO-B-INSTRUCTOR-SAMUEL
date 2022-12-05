'''Crea una funcion que calcule la potencia de un motor 
en W ya que necesitan equipar una bomba para elevar el
agua a una altura de (numero ingresado por el usuario)
con un caudal de (numero ingresado por el usuario) 
litrs/min'''
def w(altura,litros):
    minuto=60
    gravedad=9.8
    trabajo=litros*gravedad*altura
    potencia=trabajo//minuto
    print(f'La potencia del motor en w al realizar todo el procedimiento es de {potencia} W')

altura=float(input('¿A cuanta altura se elevara el agua (metros)?' ))
litros=float(input('¿Cuantos litros de agua tiene el caudal?(litros) '))
w(altura,litros)