'''
Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha
función en un programa principal que lea el radio de una circunferencia y muestre su área
y perímetro.
'''

def areaPerimetro(radio):
    area = 3.14 * (radio ** 2)
    perimetro = (2 * 3.14) * radio
    print(f'El area de la circunferencia es {round(area,2)}')
    print(f'El perimetro de la circunferencia es {round(perimetro,2)}')

print('-'*20,'AREA Y PERIMETRO DE UN CIRCULO','-'*20)
print()
radio = float(input('Cual es el radio de la circunferencia?\n-'))
areaPerimetro(radio)