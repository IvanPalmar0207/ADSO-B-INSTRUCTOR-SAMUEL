import requests
import json

#URL no dinamica y sin parametros
url = requests.post('https://httpbin.org/post')
response = url.content.decode()
print(response)

#URL dinamica y con parametros
args1={
    'nombre':'Ivan Palmar',
    'Programa':'ADSO'
}

header={
    'date':'Tue, 24 Oct 2023 13:03:36 GMT',
    'server': 'gunicorn/19.9.0'
}

#url1 = requests.post('https://httpbin.org/post',json=args1)
#url1 = requests.post('https://httpbin.org/post',data=args1)
#url1 = requests.post('https://httpbin.org/post',params=args1)
url1 = requests.post('https://httpbin.org/post',data=json.dumps(args1),headers=header)

response1 = url1.content.decode()
print(response1)