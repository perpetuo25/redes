import requests
from decouple import config
sort_ram = []
def get_ram(url):    
    response2 = requests.get(url+"/getram")
    ram = response2.json().get("ram")
    return float(ram)

def get_max_ram(urls):
    ram = urls[0]
    for i in urls:
        if get_ram(i) > get_ram(ram):
            ram = i
    return ram

def get_other_elements(urls, element):
    new_array = []
    for i in range(len(urls)):
        if urls[i] != element:
            new_array.append(urls[i])
    return new_array

def select_star(urls):
    sorted_host = []
    max_ram = get_max_ram(urls)
    sorted_host.append(max_ram)
    sorted_host.extend(get_other_elements(urls, max_ram))
    return sorted_host

