import requests

url = 'https://api.github.com/users'

#Inicia la sesion para iniciar las cookies
session = requests.Session()

#Se hace la autentificacion a traves de usuario y contraseña0
session.auth = ('palmar.ivan0205@gmail.com','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')

#Se llama la url a traves del metodo get pero de la sesion
response = session.get(url)
print(response.status_code)

#El metodo ok valida si la peticion fue correcta
if response.ok:
    #Se hace un metodo get para la direccion de mi cuenta en gitHub
    response = session.get('https://github.com/IvanPalmar0207')
    print(response.cookies)