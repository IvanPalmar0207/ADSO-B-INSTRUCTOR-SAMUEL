import requests

url = 'https://api.github.com/users'

#Inicia la sesion para iniciar las cookies
session = requests.Session()

#Se trae el get atraves de la sesion
response = session.get(url,auth=('palmar.ivan0205@gmail.com','Teresa0205.'))

print(response.status_code)