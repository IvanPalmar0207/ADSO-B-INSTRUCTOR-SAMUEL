'''En un juego de preguntas a las que responde "si"o"no" gana quien
responda correctamente a las tres preguntas. Si respone mal cualquiera
de ellas ya no se pregunta la siguiente y termina el juego'''

import sys

rcorrecta=1 
rincorrecta=2

pregunta1=int(input("El siguiente test contara de tres preguntas, elija 1 para si y 2 para no\n" "¿Cristobal Colon descubrio America?\n"))

if pregunta1!=rincorrecta:
    print("La respuesta es correcta")
else:
    print(sys.exit("La respuesta es incorrecta"))

pregunta2=int(input("¿La independencia de Colombia fue en el 1810?\n"))

if pregunta2!=rincorrecta:
            print("La respuesta es correcta")
else:
    print(sys.exit("La respuesta es incorrecta"))

preugnta3=int(input("¿The doors fue un grupo de rock americano?\n"))

if preugnta3!=rincorrecta:
    print("La respuesta es correcta")
else:    
    print(sys.exit("La respuesta es incorrecta"))
