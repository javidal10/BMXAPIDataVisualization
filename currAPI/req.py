import requests
import json


base_url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP68257/datos'
url = base_url
headers = {'Bmx-Token':'946afc3e778367dd3d2e678c632fe64b196d3b305de85b1f33f373192c9b9712'}
response = requests.get(url,headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    


        
