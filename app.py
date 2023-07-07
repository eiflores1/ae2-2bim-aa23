"""
    Ejemplo del manejo de hilos
"""

import requests
import time
import csv
import threading
# librería de python que permite ejecutar comandos
import subprocess

def obtener_data():
    lista = []
    with open("informacion/data.csv") as archivo:
        lineas = csv.reader(archivo, quotechar="|")
        for row in lineas:
            print(row[0].split("|"))
            numero = row[0].split("|")[0]
            pagina = row[0].split("|")[1]
            lista.append((numero, pagina))
# se retorna la lista con la información que se necesita
    return lista

def worker(numero, url):
    print("Iniciando %s %s" % (threading.current_thread().getName(), url ))
    # pass
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
