'''Realizar una funcion de la fomula cuadratica y corregir sus errores'''
import math
def raiz(a=int(input('Ingresa tu primer numero ')),
         b=int(input('Ingresa el segundo numero ')), 
         c=int(input('Ingresa el tercer numero '))):
    try:
        x1=(-b-math.sqrt((b**2-4*a*c)))/(2*a)
        x2=(-b+math.sqrt((b**2-4*a*c)))/(2*a)
        resultado=[x1,x2]
        print(f'El resultado de la formula cuadratica negativa es {x1}\n')
        print(f'El resultado de la formula cuadratica positiva es {x2}\n')
        print(f'El resultado de ambas es {resultado}\n')
    except ZeroDivisionError:
        print('Los argumentos no se pueden dividir por cero, es una indeterminacion')
    except ValueError:
        print('La raiz cuadrada no puede ser negativa')
    except:
        print('Ha aparecido un error indeterminado') 
raiz()