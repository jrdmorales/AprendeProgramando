"""
Algoritmos y estructuras de datos:
Prepárate para resolver problemas de algoritmos básicos como ordenar una lista, 
buscar el número máximo o mínimo, o implementar funciones recursivas.
"""

#Ejemplo clásico: Implementa una función para invertir una cadena
def invertir_cadena(cadena):
    return cadena[::-1]

#Ejemplo: Invertir una cadena
cadena = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena)
print(cadena_invertida)  # Resultado: "!odnum ,aloH"

#Ejemplo clásico: Implementa una función para ordenar una lista
def ordenar_lista(lista):
    return sorted(lista)

#Ejemplo: Ordenar una lista
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_ordenada = ordenar_lista(mi_lista)
print(lista_ordenada)  # Resultado: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

#Ejemplo clásico: Implementa una función para buscar el número máximo en una lista
def maximo_lista(lista):
    return max(lista)

#Ejemplo: Encontrar el número máximo en una lista
mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximo = maximo_lista(mi_lista)
print(maximo)  # Resultado: 9