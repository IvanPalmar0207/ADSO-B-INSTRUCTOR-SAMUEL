'''
Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una 
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “.
Crea un programa principal donde se use dicha función.
'''

def convertirEspaciado(cadena):
    for i in cadena:
        print(i, end=' ')
    
print('-'*20,'COMPARAR PALABRAS','-'*20)
nombre = input('Cual es tu nombre?\n-')
correoElectronico = input('Cual es tu correo eletronico?\n-')
direccion = input('Cual es tu direccion?\n-')
print('\nPalabras sin separacion')
print(f'Tu nombre es: {nombre}\nTu correo electronico es: {correoElectronico}\nTu direccion es: {direccion}')
print()
print('Palabras separadas')
print('Nombre:')
convertirEspaciado(nombre)
print('\nCorreo Electronico:')
convertirEspaciado(correoElectronico)
print('\nDireccion')
convertirEspaciado(direccion)