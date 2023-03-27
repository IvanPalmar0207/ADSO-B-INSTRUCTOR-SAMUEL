import sqlite3
with sqlite3.connect('C:\\Users\\SENA\\Documents\\ivan_palmar\\ADSO-B-INSTRUCTOR-SAMUEL\\15avo_Miscelania_(PROYECTO)\\prueba_(PROYECTO).db') as goku:
    micursor=goku.cursor()

def insertarTpUssuario(conexion,tabla,c1,dato1):
    micursor=conexion.cursor()
    sentenciainsert=f'INSERT INTO {tabla} ({c1}) VALUES ("{dato1}")'
    micursor.execute(sentenciainsert)
    goku.commit()
    print('La insercion del dato fue creado')
#insertarTpUssuario(goku,'tb_tipoUsuario','Tipo_TpU','Prueba-ADSO')

def selectALL(conexion,tabla):
    micursor=conexion.cursor()
    sentenciaselectall=f'SELECT * FROM {tabla}'
    print(micursor.execute(sentenciaselectall).fetchall())
#selectALL(goku,'tb_tipoUsuario')

def selectId(conexion,tabla,condicionid):
    micursor=conexion.cursor()
    sentencia=f'SELECT * FROM {tabla} WHERE Id_TpU="{condicionid}"'
    print(micursor.execute(sentencia).fetchall())
#selectId(goku,'tb_tipoUsuario',7)

def updateId(conexion,tabla,nombre,id):
    micursor=conexion.cursor()
    sentencia=f'UPDATE {tabla} SET Tipo_TpU="{nombre}" WHERE Id_TpU="{id}"'
    micursor.execute(sentencia)
    goku.commit()
updateId(goku,'tb_tipoUsuario','Saiyajin',1)

def updateNombre():

def deleteTU(:)