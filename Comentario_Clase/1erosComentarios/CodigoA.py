try:#Se hace uso de la palabra reservada try para tratar el siguiente bloque de codigo y evaluar su posibles errores.
    #print(1/1)) #Esta parte del codigo se encuentra comentada ya que un error de syntasis recae unicamente sobre el programador.
    raise SyntaxError #Se arroja una excepcion manualmente en este caso la excepcion SyntaxError con el metodo raise.
except SyntaxError: #Se trata la excepcion SyntasError por medio de la palabra reservada except la cual evaluara el fragmento de codigo del try y si ocurre el error vendra aqui.
    print('Cierra el parentesis') #Si el error fue de sintaxis entonces se imprimira el mensaje que esta entre los parentesis.