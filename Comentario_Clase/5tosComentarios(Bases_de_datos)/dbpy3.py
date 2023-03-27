import sqlite3 #Se hace uso de la palabra reservada import que sirve para importar un modulo o un paquete, en este caso se hara una importacion de un paquete llamado sqlite3 que sirve para la manipulacion de bases de datos serverless(sin servidor) creadas en sqlite3.
con=sqlite3.connect('C:\\narvaez\\db\\conpython.db') #Se instancia un nuevo objeto para el modulo sqlite3 
print(type(con))
micursor=con.cursor()
print(type(micursor))