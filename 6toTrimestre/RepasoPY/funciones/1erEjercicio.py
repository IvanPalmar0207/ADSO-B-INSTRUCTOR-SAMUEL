'''
Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado 
en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 
espacios antes del texto). Además subraya el mensaje utilizando el carácter =.
'''

def escribirCentrado(texto):
    longitud = len(texto)*2
    resultado = texto.center(longitud,'=')
    return resultado

print('-'*20,'TEXTO CENTRADO','-'*20)
textoIngreso = input('Ingresa un texto para centrar: ')
print(escribirCentrado(textoIngreso))