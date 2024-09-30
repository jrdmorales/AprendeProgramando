### entrevista de desarrollador Python junior o trainee
Para una entrevista de desarrollador Python junior o trainee, aquí te dejo algunos puntos clave que suelen tocarse en este tipo de entrevistas y cómo puedes abordarlos:

1.  Preguntas Técnicas sobre Python:
- Sintaxis y estructuras básicas: Asegúrate de dominar las listas, diccionarios, tuplas, conjuntos y cómo iterar sobre ellos.
    - Ejemplo: ¿Cómo se agrega un elemento a una lista?
        mi_lista = [1, 2, 3]
        mi_lista.append(4)  # Resultado: [1, 2, 3, 4]

- Comprensiones de listas y diccionarios:
    - Ejemplo: Generar una lista de números al cuadrado.
        cuadrados = [x**2 for x in range(10)]

- Manejo de errores y excepciones: Conocer cómo usar try, except y manejar excepciones comunes como IndexError o KeyError. 
        try:
            mi_lista[10]
        except IndexError:
            print("Índice fuera de rango")

2. Algoritmos y estructuras de datos:
- Prepárate para resolver problemas de algoritmos básicos como ordenar una lista, buscar el número máximo o mínimo, o implementar funciones recursivas.

    - Ejemplo clásico: Implementa una función para invertir una cadena.
        def invertir_cadena(cadena):
            return cadena[::-1]

3. Manipulación de archivos:
- Saber abrir, leer y escribir archivos es una habilidad fundamental.
    - Ejemplo: Leer un archivo de texto y contar las palabras

        with open('archivo.txt', 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            print(f"El archivo tiene {len(palabras)} palabras.")

4. Conocimiento sobre bibliotecas estándar:
- Familiarízate con bibliotecas como os para manipular archivos y carpetas, datetime para manejo de fechas, o re para expresiones regulares.
     - Ejemplo: Usar os para listar archivos en un directorio.

           import os
            archivos = os.listdir('.')
            print(archivos)


5. Entendimiento de OOP (Programación Orientada a Objetos):
- Aunque las posiciones de junior pueden no requerir un conocimiento profundo, es importante entender conceptos básicos como clases, objetos, herencia y encapsulamiento.
  - Ejemplo: Definir una clase simple
        class Perro:
            def __init__(self, nombre, raza):
                self.nombre = nombre
                self.raza = raza

            def ladrar(self):
                print(f"{self.nombre} está ladrando.")

        mi_perro = Perro("Rex", "Labrador")
        mi_perro.ladrar()

6. Preguntas sobre bases de datos:
- Aunque en algunos casos podrías no tener experiencia, es útil saber cómo interactuar con una base de datos simple usando sqlite3 o cómo hacer queries básicas en SQL.
    - Ejemplo: Conectar y hacer una consulta en una base de datos SQLite
        import sqlite3
        conexion = sqlite3.connect('mi_base_de_datos.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultado = cursor.fetchall()
        print(resultado)
        conexion.close()

7. Preguntas de lógica y resolución de problemas:
- Te pedirán resolver problemas lógicos o de programación en vivo. Practicar en plataformas como LeetCode, HackerRank o Codewars te ayudará a mejorar tus habilidades para resolver estos retos.
    - Ejemplo: Escribir una función que determine si una palabra es un palíndromo
        def es_palindromo(palabra):
        return palabra == palabra[::-1]

8. Versionamiento con Git:
-  Conocer comandos básicos de Git, como clone, add, commit, push, y cómo trabajar con ramas (branch).
    - Ejemplo: Agregar cambios y hacer un commit
        git add .
        git commit -m "Agregando nueva funcionalidad"
        git push origin main

9. Preguntas de comportamiento:
- Las entrevistas también pueden tener preguntas como
    ¿Por qué te interesa esta posición?
    ¿Cómo manejas los errores?
    ¿Te sientes cómodo trabajando en equipo?

10. Proyectos personales:
    Si tienes proyectos que puedas mostrar (en Python o cualquier otro lenguaje), asegúrate de estar preparado para explicar qué hiciste, qué problemas resolviste y qué tecnologías utilizaste. Esto es especialmente importante para un perfil junior.

### Preguntas comunes en una entrevista de Python Junior:
1. ¿Qué diferencia hay entre una lista y una tupla?
2. ¿Cómo manejas errores en Python?
3. ¿Qué son las comprensiones de listas (list comprehensions)?
4. ¿Qué es PEP 8 y por qué es importante?
5. ¿Puedes explicar el concepto de herencia en Python?
6. ¿Cómo crearías una API REST simple en Python?
7. ¿Has trabajado con Git? ¿Qué comandos usas con frecuencia?
8. ¿Cómo gestionarías un conflicto de merge en Git?

