import requests

#Se hace el inicio de sesion
sesion = requests.session()

#Se autentifica el usuario con sus credenciales, nombre de usuario y contraseña
sesion.auth = ('palmar.ivan0205@gmail.com','Teresa0205.')

#Se hace el llamado de la url por el metodo GET del sitio principal
response = sesion.get('https://drive.google.com/drive')
#Impresion del estado de la peticion
print(response.status_code)

if response.ok:
    #Se hace una peticion con la URL independiente
    response = sesion.get('https://drive.google.com/drive/my-drive')
    print(response.cookies)