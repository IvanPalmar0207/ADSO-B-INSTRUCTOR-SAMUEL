import requests

url = 'https://httpbin.org/cookies'

#Creacion de Cookies
myCookies = {
    'cookie':'True'
}

#Respuesta a la peticion, uso de cookies creadas desde el cliente
response = requests.get(url,cookies=myCookies)
print(response.content)
print('-'*50)
print(response.cookies)