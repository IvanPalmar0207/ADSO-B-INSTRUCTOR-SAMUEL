import requests

url = ('https://api.covidtracking.com/v2/states.json')
response = requests.get(url)
data = response.json()
#Tipo de datos de data
#print(type(data))

#Llenar la lista por comprension
comprension = [clave['name'] for clave in data['data']]
print(comprension)

#Visualizacion del nombre en menos lineas de codigo
nombreCiudades = []

for i in data['data']:
    nombreCiudades.append(i['name'])

#Visualizacion de datos dentro de la lista
print(nombreCiudades)
#Visualizacion de datos independientes
for i in nombreCiudades:
    print(i, end=' ')