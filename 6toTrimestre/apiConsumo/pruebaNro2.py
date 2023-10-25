import requests

url = ('https://www.datos.gov.co/resource/ucni-bnem.json')
request = requests.get(url)
response = request.json()