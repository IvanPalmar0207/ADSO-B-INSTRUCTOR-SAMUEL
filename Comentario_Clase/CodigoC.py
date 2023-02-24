def try_syntax(numerator, denominator): #Se crea una funcion(try_syntax) con dos argumentos(numerator, denominator)
    try:#Se hace uso de la palabra reservada try la cual evaluara el siguiente fragmento de codigo
        print(f'In the try block: {numerator}/{denominator}') #Se imprime con el metodo f un mensaje y ambos argumentos ya puestos por el usuario en manera de division
        result = numerator / denominator
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print('The result is:', result)
        return result
    finally:
        print('Exiting')
print(try_syntax(11, 0))