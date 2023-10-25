#Se importa la libreria Requests
import requests
#En un variable se captura la URL de la imagen
url = ('https://cdn-icons-png.flaticon.com/512/3938/3938028.png')
#En un variable se guarda la url de donde viene la imagen y si el hay flujo o no
request = requests.get(url,stream=True)
#Se crea un archivo que guarde la imagen, se itera y se guarda con el alias para escribir en el archivo
with open('protocoloHttp/twitter.png','wb') as pythonImage:
    for i in request.iter_content():
        pythonImage.write(i)