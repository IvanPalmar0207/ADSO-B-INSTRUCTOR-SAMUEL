import requests
import json

args={
    'Nombre':'Goku Martinez',
    'Profesion':'Panadero'
}
request1 = requests.put('https://httpbin.org/put',params=args)
request2 = requests.put('https://httpbin.org/put',json=args)
request3 = requests.put('https://httpbin.org/put',data=args)
request4 = requests.put('https://httpbin.org/put',data=json.dumps(args))

response1 = request1.content.decode()
print(response1)
print('-'*50)

response2 = request2.content.decode()
print(response2)
print('-'*50)

response3 = request3.content.decode()
print(response3)
print('-'*50)

response4 = request4.content.decode()
print(response4)
print('-'*50)