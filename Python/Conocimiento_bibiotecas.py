"""
Conocimiento sobre bibliotecas estándar:
Familiarízate con bibliotecas como os para manipular archivos y carpetas, datetime para manejo de fechas, o re para expresiones regulares.
"""

#Ejemplo: Usar os para listar archivos en un directorio
import os
def listar_archivos():
    import os
    archivos = os.listdir('.')
    return archivos

print(listar_archivos())

#Ejemplo: Usar datetime para obtener la fecha y hora actual
import datetime
def obtener_fecha_actual():
    import datetime
    ahora = datetime.datetime.now()
    return ahora
print(obtener_fecha_actual())

#Ejemplo: Usar re para buscar coincidencias de patrones en un texto
import re
def buscar_coincidencias(texto, patron):
    import re
    coincidencias = re.findall(patron, texto)
    if coincidencias:
        print("Se encontraron coincidencias.")
    else:
        print("No se encontraron coincidencias.")
    return coincidencias

texto = "Python es un lenguaje de programación muy poderoso."
patron = "Python"
print(buscar_coincidencias(texto, patron))

#Ejemplo: Usar random para generar números aleatorios
import random
def generar_numero_aleatorio():
    import random
    numero_aleatorio = random.randint(1, 10)
    return numero_aleatorio

print(generar_numero_aleatorio())


#Ejemplo: Usar math para funciones matemáticas
import math
def calcular_raiz_cuadrada(numero):
    import math
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada

print(calcular_raiz_cuadrada(16))


#Ejemplo: Usar json para trabajar con datos en formato JSON

import json
def datos_json():
    datos = '{"nombre": "Alice", "edad": 25}'
    datos_json = json.loads(datos)
    return datos_json

datos_json = datos_json()
print(datos_json['nombre'])


#Ejemplo: Usar requests para hacer solicitudes HTTP
import requests
def obtener_respuesta(url):
    respuesta = requests.get(url)
    return respuesta

respuesta = obtener_respuesta('https://www.google.com/')
print(respuesta.status_code)

#Ejemplo: Usar sqlite3 para trabajar con bases de datos SQLite
import sqlite3
def crear_tabla():
    conexion = sqlite3.connect('ejemplo.db')
    cursor = conexion.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)')
    conexion.commit()
    conexion.close()

crear_tabla()

#Ejemplo: Usar smtplib para enviar correos electrónicos
import smtplib
def enviar_correo():
    servidor_correo = smtplib.SMTP('smtp.gmail.com', 587)
    servidor_correo.starttls()
    servidor_correo.login('servidor_correo.sendmail')
    servidor_correo.quit()

enviar_correo()

#Ejemplo: Usar tkinter para crear interfaces gráficas
import tkinter as tk
def crear_ventana():
    ventana = tk.Tk()
    etiqueta = tk.Label(ventana, text='¡Hola, mundo!')
    etiqueta.pack()
    ventana.mainloop()

crear_ventana()

