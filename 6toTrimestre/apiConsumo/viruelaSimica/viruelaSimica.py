import requests

url = 'https://www.datos.gov.co/resource/tmet-yeek.json'
request = requests.get(url)
response = request.json()