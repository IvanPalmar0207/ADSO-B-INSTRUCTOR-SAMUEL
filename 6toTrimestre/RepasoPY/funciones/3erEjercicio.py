'''
Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima
y mínima. Crear un programa principal, que utilizando la función anterior, vaya pidiendo la 
temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número
de días que se van a introducir.
'''
def temperaturaMedia(temperaturaMaxima,temperaturaMinima):
    temperaturaMedia = (temperaturaMaxima+temperaturaMinima)/2
    return temperaturaMedia

print('-'*20,'TEMPERATURA MEDIA','-'*20)

dias = int(input('Cuantos dias van a ser calculados?\n-'))
print()
contador = 0
while True:
    contador+=1
    print(f'Temperatura del dia {contador}\n')
    temperaturaMaxima = float(input('Cual fue la temperatura maxima: '))        
    temperaturaMinima = float(input('Cual fue la temperatura minima: '))
    if temperaturaMaxima<temperaturaMinima:
        print('La temperatura maxima tiene que ser mayor a la minima\n')
        break
    else:
        print(f'La temperatura media del dia {contador} fueron {temperaturaMedia(temperaturaMaxima,temperaturaMinima)} grados\n')
        if contador<dias:
            continue
        else:
            print('El calculo ha terminado, muchas gracias señor usuario\n')
            break 