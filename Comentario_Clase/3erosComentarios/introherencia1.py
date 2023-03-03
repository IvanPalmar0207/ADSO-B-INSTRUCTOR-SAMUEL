def suma (a,b):#Aqui se declara una funcion con la palabra reservada def, se le asigna un nombre el cual es suma, con dos parametros que son a y b y se cierra con dos puntos.
    return a+b#Este return retorna la suma de a + b.
def suma(a,b,c):#Se hace una nueva declaracion de funcion con la palabra reservada def y con el mismo nombre de la anterior funcion osea suma, pero en este caso se le asignan tres parametros a la lista de parametros de la funcion.
    return a+b+c#Aqui el return retorna la suma de los tres parametros (a+b+c).
print(suma(1,2,3))#Este print imprimira la funcion que fue declara de segundas ya que remplaza a la funcion que fue declarada de primeras ya que python es un lenguaje interpretado que va traduciendiendo linea a linea cada parte del codigo no como los lenguajes no compilados que traducen todo el codigo escrito por el programador, esto quiere decir que aqui se identifica como si la funcion suma hubiera sido declarada una segunda vez pero con tres parametros esto quiere decir que python no deja hacer sobreescritura de funciones, simplemente si se escribe una funcion con el mismo nombre a una ya escrita y su estructura es diferente se tomara como si hubiera sido declara nuevamente osea la primera funcion no se podra realizar o utilizar.
#Esto quiere decir que python no implementa el polimorfismo de la manera que lo hacen los lenguajes compilados o 100% hechos para POO como Java o C++.