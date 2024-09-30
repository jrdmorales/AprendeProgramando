"""
Manipulación de archivos:
Saber abrir, leer y escribir archivos es una habilidad fundamental.

"""

#Ejemplo: Leer un archivo de texto y contar las palabras.

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    palabras = contenido.split()
    print(f"El archivo tiene {len(palabras)} palabras.")


#Ejemplo: Escribir en un archivo de texto.

with open('nuevo_archivo.txt', 'w') as archivo:
    archivo.write("¡Hola, mundo!")
    archivo.write("\n")
    archivo.write("¡Adiós, mundo!")
    archivo.write("\n")
    archivo.write("¡Hola, de nuevo!")

#Ejemplo: Leer un archivo CSV y procesar los datos.

import csv

with open('datos.csv', 'r') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)

#Ejemplo: Escribir en un archivo CSV.

datos = [
    ['Nombre', 'Edad', 'Género'],
    ['Alice', '25', 'Femenino'],
    ['Bob', '30', 'Masculino'],
    ['Charlie', '35', 'Masculino']
]

with open('nuevos_datos.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    for fila in datos:
        escritor_csv.writerow(fila)