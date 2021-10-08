import psutil    
ram = psutil.virtual_memory().total / 1e+9
print(ram)

