import requests
import json

args={
    'Nombre':'Lionel Messi',
    'Profesion':'Futbolista Profesional'
}
request1 = requests.delete('https://httpbin.org/delete',params=args)
request2 = requests.delete('https://httpbin.org/delete',json=args)
request3 = requests.delete('https://httpbin.org/delete',data=args)
request4 = requests.delete('https://httpbin.org/delete',data=json.dumps(args))

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