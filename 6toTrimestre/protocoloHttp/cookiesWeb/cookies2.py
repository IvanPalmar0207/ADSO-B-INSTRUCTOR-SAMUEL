import requests

url = 'https://api.github.com/users'

#Inicia la sesion para iniciar las cookies
session = requests.Session()

#Se trae el get atraves de la sesion
response = session.get(url,auth=('palmar.ivan0205@gmail.com','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'))

print(response.status_code)