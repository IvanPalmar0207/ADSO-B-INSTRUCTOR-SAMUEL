'''Telfonica realiza los calculos del costo de una llamada
siguiendo los calculos asi: Cuando se descuelga el telefono
los primeros 3 minutos (banderazo) cuestan 200 pesos y cada
minuto adicional cuesta 50 pesos. Escriba un programa dados
los minutos de duracion'''


duracion=int(input("Ingresa la duracion de tu llamada si el usuario no descolgo el telefono o digita -1 si descolgo el telefono: "))

minuto=50*duracion
no_atendio=-1

if duracion>=1:
    print("El usuario atendio la llamada y el costo fue: ", minuto,"pesos")
else:
    print("El usuario descolgo el telefono")    


d=int(input("Ingresa la duracion de la llamada del usuario si descolgo el telefono o escribe -1 si el usuario atendio: "))
banderazo=200

b2=50+(50*d)

atendio=-1
if d >= 1 and d <=3:
    print("Si el usuario descolgo el telefono los primeros tres minutos el costo de la llamada fue: ", banderazo,"pesos")
elif d >=4:
    print("Si el usuario no descolgo antes de los tres minutos el costo de la llamada fue: ", b2, "pesos")
else:
    print("El usuario si atendio la llamada")    