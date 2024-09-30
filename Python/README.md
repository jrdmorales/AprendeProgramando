### Entrevista de desarrollador Python junior o trainee
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
        - ¿Por qué te interesa esta posición?
        - ¿Cómo manejas los errores?
        - ¿Te sientes cómodo trabajando en equipo?

10. Proyectos personales:
   - Si tienes proyectos que puedas mostrar (en Python o cualquier otro lenguaje), asegúrate de estar preparado para explicar qué hiciste, qué problemas resolviste y qué tecnologías utilizaste. Esto es especialmente importante para un perfil junior.

### Preguntas comunes en una entrevista de Python Junior:
1.  ¿Qué diferencia hay entre una lista y una tupla?
   - Lista:
        - Mutable: Puedes modificarla, agregar o eliminar elementos después de haber sido creada. se define con corchetes [].
   - Tupla:
       - Inmutable: Una vez creada, no se puede modificar (no puedes agregar, eliminar o cambiar elementos). Se define con paréntesis ()
         
2.  ¿Cómo manejas errores en Python?
   - En Python, los errores o excepciones se manejan utilizando los bloques try-except. Puedes capturar errores específicos y evitar que el programa se detenga de forma abrupta.

3.  ¿Qué son las comprensiones de listas (list comprehensions)?
   - Las comprensiones de listas son una manera concisa de crear listas en Python a partir de una secuencia o iterable, aplicando alguna operación a cada elemento y/o filtrando elementos según alguna condición.

4.  ¿Qué es PEP 8 y por qué es importante?
   - PEP 8 es una guía de estilo para escribir código Python que establece convenciones sobre cómo formatear el código para que sea más legible y consistente entre desarrolladores.

- Algunos puntos clave de PEP 8 incluyen:
    - Indentación: Usar 4 espacios por nivel de indentación.
    - Longitud de línea: No debe exceder de 79 caracteres.
    - Nombres de variables: Nombres en minúsculas y con guiones bajos para separar palabras (mi_variable).
    - Comentarios: Los comentarios deben ser claros y descriptivos.
    - Espacios: No debe haber espacios innecesarios alrededor de operadores, comas o paréntesis.
     Es importante porque facilita la lectura y mantenimiento del código, especialmente cuando múltiples desarrolladores 
     colaboran en el mismo proyecto.

5.  ¿Puedes explicar el concepto de herencia en Python?
   - La herencia es un principio de la Programación Orientada a Objetos (POO) que permite crear una nueva clase basada en una clase existente, reutilizando el código.

- La clase existente se llama clase padre o superclase.
- La nueva clase se llama clase hija o subclase.

6.  ¿Cómo crearías una API REST simple en Python?
- Una API REST se puede crear fácilmente en Python utilizando un framework como Flask. Aquí un ejemplo básico de una API - - REST que permite manejar usuarios:

       from flask import Flask, jsonify, request
        
        app = Flask(__name__)
        
        # Datos simulados
        usuarios = [
            {'id': 1, 'nombre': 'usuario1'},
            {'id': 2, 'nombre': 'usuario2'}
        ]
        
        # Ruta para obtener todos los usuarios
        @app.route('/usuarios', methods=['GET'])
        def obtener_usuarios():
            return jsonify(usuarios)
        
        # Ruta para obtener un usuario por su ID
        @app.route('/usuarios/<int:id>', methods=['GET'])
        def obtener_usuario(id):
            usuario = next((u for u in usuarios if u['id'] == id), None)
            return jsonify(usuario) if usuario else ('Usuario no encontrado', 404)
        
        # Ruta para agregar un nuevo usuario
        @app.route('/usuarios', methods=['POST'])
        def agregar_usuario():
            nuevo_usuario = request.json
            usuarios.append(nuevo_usuario)
            return jsonify(nuevo_usuario), 201
        
        if __name__ == '__main__':
            app.run(debug=True)

  
- GET /usuarios para obtener todos los usuarios.
- GET /usuarios/<id> para obtener un usuario por ID.
- POST /usuarios para agregar un nuevo usuario.

7.  ¿Has trabajado con Git? ¿Qué comandos usas con frecuencia?
- Sí, he trabajado con Git para control de versiones y colaboración en proyectos. Los comandos que uso con frecuencia son:
    - git clone: Clonar un repositorio remoto en mi máquina local.
    - git add: Agregar cambios al área de staging.
    - git commit: Crear un commit con un mensaje descriptivo.
    - git push: Enviar los cambios locales al repositorio remoto.
    - git pull: Descargar y fusionar los cambios del repositorio remoto a mi copia local.
    - git branch: Listar o crear ramas.
    - git checkout: Cambiar de una rama a otra.
  
8.  ¿Cómo gestionarías un conflicto de merge en Git?
  - Un conflicto de merge ocurre cuando dos ramas modifican la misma parte de un archivo de manera incompatible. Para resolverlo:
  1. Realiza el merge:

         git merge rama-feature

  2. Git detectará el conflicto y te avisará. Luego, abre el archivo en conflicto, donde verás algo como esto:

            <<<<<<< HEAD
            Esta es la versión en la rama principal.
            =======
            Esta es la versión en la rama-feature.
            >>>>>>> rama-feature

  
  3. Edita el archivo para resolver el conflicto, eligiendo qué cambios mantener o combinarlos.

  4. Después de resolver los conflictos, marca el archivo como resuelto:

          git add archivo_en_conflicto.py

  5. Finalmente, crea un commit que complete el merge:

          git commit -m "Resuelto conflicto de merge"
 Con esto habrás gestionado el conflicto y completado el merge.

