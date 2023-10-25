import requests

url = ('https://api.covidtracking.com/v2/states.json')
response = requests.get(url)
data = response.json()
#Tipo de datos de data
#print(type(data))

#Llenar la lista por comprension
comprension = [(i,y) for i in data.keys() for y in data['data']]

#Visualizacion del nombre en menos lineas de codigo
nombreCiudades = []

for key in data.keys():
    for key1 in data['data']:
        for i in key1:
            resultado = key1['name']
            nombreCiudades.append(resultado)

#Visualizacion de datos dentro de la lista
print(nombreCiudades)

#Visualizacion de datos independientes
for i in nombreCiudades:
    print(i, end=', ')