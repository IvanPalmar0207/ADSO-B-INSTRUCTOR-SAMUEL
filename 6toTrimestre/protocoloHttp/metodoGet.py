import requests
import json

#URL no dinamica
url = requests.get('https://httpbin.org/get?nombre=Lionel Messi&edad=34')
response = url.content.decode()
print(response)

#URL dinamica
url = 'https://httpbin.org/get'
args = {
    'nombres':'Lionel Messi',
    'edad':34
}
response2 = requests.get(url,params=args)
rta = response2.content.decode()

#Conversion de la solicitud a un diccionario
rta = response2.json()
print(rta)