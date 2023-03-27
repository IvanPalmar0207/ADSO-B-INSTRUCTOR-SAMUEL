
import sqlite3

with sqlite3.connect('C:\\Users\\SENA\\Documents\\ivan_palmar\\ADSO-B-INSTRUCTOR-SAMUEL\\Comentario_Clase\\5tosComentarios(Bases_de_datos)\\conpython.db')as con:
    micursor=con.cursor()
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"
    #print(micursor.execute(sentencia).fetchall())

def select(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())

select(con,'alumno','email','=','dbrabon2@irs.gov')

def modificar(conex,tabla,campo,dato,id):
    micursor=conex.cursor()
    sentencia1=f'UPDATE {tabla} SET {campo}="{dato}" WHERE id={id}'
    micursor.execute(sentencia1)
    con.commit()
    print('Actualizacion Exitosa¡')
modificar(con,'alumno','nombre','Kakaroto',1)

def eliminar(conex,table,campo,dato):
    micursor=conex.cursor()
    sentencia2=f'DELETE FROM {table} where {campo}={dato}'
    micursor.execute(sentencia2)
    con.commit()
    print('Eliminacion Exitosa')
eliminar(con,'alumno','id',2)