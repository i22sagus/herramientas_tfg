# calcular_media.py
# Este programa proporciona estadísticas sobre las notas de los alumnos sin utilizar librerías

import json

with open("notas.json", encoding="utf8") as f:
    datos=json.load(f)

# -Nota media de matemáticas-
suma = 0
for alumno in datos:
    suma+=alumno["matematicas"]

media=suma/len(datos)
# len() cuenta los elementos
print(f"1Media de los alumnos en matemáticas: {media:.2f}") 

# -Nota media utilizando "list comprehension"-
# construye una lista nueva en una sola línea
lista_mates = [a["matematicas"] for a in datos]
# round(x, n) redondea a 2 decimales
# sum() suma los elementos de la lista
print("Media calculada con list comprehension:", round(sum(lista_mates) / len(lista_mates), 2))


# -Nota más alta de la clase-
# max() devuelve el mayor valor de una lista pero la lista contiene
# DICCIONARIOS, y Python no sabe cuál de dos diccionarios es "mayor".
# Con key=... le indicamos que criterio usar para comparar.
#
# 'lambda a: a["matematicas"]' es una función sin nombre. Funciona asi: "
# dado un alumno 'a', devuelve su nota de matemáticas".
# max() la aplica a cada alumno y se queda con el que dé el valor más alto.
# max devuelve el ALUMNO entero (el diccionario), no solo la nota.

mejor = max(datos, key=lambda a: a["matematicas"])
print(f"Nota mas alta: {mejor['nombre']} con {mejor['matematicas']}")


# -Alumnos suspensos-
suspensos = 0
for alumno in datos:
    if alumno["matematicas"] < 5:
        suspensos+=1
        print("Suspende: ", alumno["nombre"])

print("Total de suspensos: ", suspensos)