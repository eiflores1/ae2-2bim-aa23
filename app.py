#Tarea 2.2 POA

import requests
import time
import csv
import threading
import os

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            print(row[0].split("|"))
            numero = row[0].split("|")[0]
            pagina = row[0].split("|")[1]
            lista.append((numero, pagina))  
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    pagina = requests.get(url)
    archivo_path = os.path.join("salida", f"{numero}.txt")
    os.makedirs(os.path.dirname(archivo_path), exist_ok=True)
    with open(archivo_path, "w") as archivo:
        archivo.write(pagina.text)
    time.sleep(10)
    print("Finalizando %s" % (threading.current_thread().getName()))

for c in obtener_data():
    # Se crea los hilos
    # en la función
    numero = c[0]
    url = c[1]
    hilo1 = threading.Thread(name='navegando...',
                            target=worker,
                            args=(numero, url))
    hilo1.start()
