from typing import cast
import requests
from decouple import config
import json as js
from itertools import cycle

URL_1 = config("HOST1", cast=str)
URL_2 = config("HOST2", cast=str)
URL_3 = config("HOST3", cast=str)

hosts = [URL_1,URL_2,URL_3]
pool = cycle(hosts)
i = 0
valor = 0
while i < 50:
    for url in hosts:
        response = requests.post(URL_1+"/suma", json={"variable": valor})
        valor = response.json().get("variable")
        print(valor)
        i = i + 1
        """
        if i %2 == 0:
        else:
            response = requests.post(URL_2+"/suma", json={"variable": valor})
            valor = response.json().get("variable")
            print(valor)
            i = i + 1
            """
