"""
Preguntas Técnicas sobre Python:
Sintaxis y estructuras básicas: Asegúrate de dominar las listas, diccionarios, tuplas, conjuntos y cómo iterar sobre ellos.

"""
#Ejemplo: ¿Cómo se agrega un elemento a una lista?
#Respuesta: Se agrega un elemento a una lista con el método append()
#Ejemplo:
mi_lista = [1, 2, 3]
mi_lista.append(4)  # Resultado: [1, 2, 3, 4]
print(mi_lista)

#Ejemplo: ¿Cómo se elimina un elemento de una lista?
#Respuesta: Se elimina un elemento de una lista con el método remove()
#Ejemplo:
mi_lista.remove(2)  # Resultado: [1, 3]
print(mi_lista)

"""
Estructuras de control: Asegúrate de entender cómo funcionan los bucles y las condicionales en Python.
"""
#Ejemplo: ¿Cómo se itera sobre una lista?
#Respuesta: Se itera sobre una lista con un bucle for
#Ejemplo:
mi_lista = [1, 2, 3, 4]
for elemento in mi_lista:
    print(elemento)

"""
Comprensiones de listas y diccionarios: Asegúrate de entender cómo funcionan las comprensiones de listas y diccionarios en Python.
"""
#Ejemplo: Generar una lista de números al cuadrado
#Respuesta: Se puede generar una lista de números al cuadrado con una comprensión de listas
#Ejemplo:
cuadrados = [x**2 for x in range(10)]

"""
Manejo de errores y excepciones: Conocer cómo usar try, except y manejar excepciones comunes como IndexError o KeyError.
"""
#Ejemplo: Manejar una excepción de índice fuera de rango
#Respuesta: Se puede manejar una excepción de índice fuera de rango con un bloque try-except
#Ejemplo:
try:
    mi_lista[10]
except IndexError:
    print("Índice fuera de rango")
