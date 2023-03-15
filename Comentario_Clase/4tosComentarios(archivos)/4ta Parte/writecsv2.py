import csv #Se usa la palabra reservada import que se usa para importar un archivo o un modulo, basicamente en este caso se importa el modulo csv que sirve para manipular archivos csv ya sea para editarlos, leerlos o escribir en ellos.
diccio=[ #Se crea una variable que se llama diccio basicamente contiene una varaible con muchos diccionarios dentro de la misma la cual tiene en cada uno dos claves y dos valores en cada diccionario dentro de la lista.
    {'name':'Alice','age':18}, #Este es el primer diccionario que se encuentra dentro de la lista, contiene una primera clave que es 'name' y su valor que es 'Alice', y en este diccionario hay una segunda clave que es 'age' que contiene como valor el numero 18.
    {'name':'Bob','age':19}, #Este es el segundo diccionario que se encuentra dentro de la lista, contiene una primera clave que es 'name' y su valor que es 'Bob', y en este diccionario hay una segunda clave que es 'age' que contiene como valor el numero 19.
    {'name':'John','age':17}] #Este es el tercer diccionario que se encuentra dentro de la lista, contiene una primera clave que es 'name' y su valor que es 'Jhon', y en este diccionario hay una segunda clave que es 'age' que contiene como valor el numero 17.
header=['name','age'] #Se crea o instancia una nueva variable local que se llama 'header' esta basicamente contiene una lista con una serie de valores, primneramente contiene 'name' y el segundo valor es 'age'.

with open('4ta Parte/people.csv','w') as csvfile: #Se usa la palabra reservada with para crear un bloque de codigo para la manipulacion del archivo csv, despues de la palabra reservada with se usa la palabra open() o metodo de archivos que sirve para abrir un archivo el cual pide dos parametros o tres en los diferentes casos, el primer parametro es para poner la ruta del archivo que se desea manipular, el segundo parametro es en que modo se desea usar el archivo si es modo leer, agregar, escribir o crear, en este caso se pone la direccion del archivo y despues se pone la letra 'w' que basicamente sirve para eliminar y escribir en el archivo, despues de los parametros viene la palabra reservada as que sirve para poner un alias al archivo y basicamente manipularlo, despues se le asigna dicho alias que en este caso 'csvfile'.
    writer=csv.DictWriter(csvfile,fieldnames=header) #Se crea una variable local que es 'writer' la cual contiene un metodo del modulo csv el cual es DictWriter, este pide dos parametros los cuales son el archivo a escribir y el segundo los nombres de campo que en este caso es la variable header que es la lista que contiene como contenido , name y age.
    writer.writeheader() #Se usa la variable local con un metodo del modulo csv el cual es writeheader() pero simplemente este es o sirve para escribir la cabecera del archivo que sera 'name' y 'age'.
    writer.writerows(diccio) #Se usa la variable local con un nuevo metodo del modulo csv el cual es writerows() que servira para escribir las filas del archivo csv que pedira simplemente un parametro, en este caso se le pasa la variable diccio que es y contiene 3 diccionarios con diferentes valores.