from typing import cast
import requests
from decouple import config
import json as js
import utils

URL_1 = config("HOST1", cast=str)
URL_2 = config("HOST2", cast=str)
URL_3 = config("HOST3", cast=str)

hosts = [URL_1,URL_2,URL_3]
start = utils.select_star(hosts)
response2 = requests.get(start[0]+"/finish")
name = response2.json().get("name")
print(name)
i = 0
last = ""
valor = 0
while i < 49:
    for url in start:
        response = requests.post(url+"/suma", json={"variable": valor})
        valor = response.json().get("variable")
        print(valor)
        last = url
        i = i + 1       
response2 = requests.get(last+"/finish")
name = response2.json().get("name")
print(name)
