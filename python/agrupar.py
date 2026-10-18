# agrupar.py
# Este programa agrupa datos utilizando diccionarios

import json
 
with open("notas.json", encoding="utf-8") as f:
    alumnos = json.load(f)


# construir un diccionario con las notas de cada grupo

notas_por_grupo = {}

for a in alumnos:
    if a["programacion"] is None:
        continue    # si encuentra None salta el resto del bloque para este alumno

    grupo = a["grupo"]


    # notas_por_grupo.setdefault(grupo, []).
    # - si la clave grupo ya existe devuelve la lista actual
    # - si no existe la crea con una lista vacia y la devuelve.
    # .append(valor): añade el valor al final de la lista
    # a["programacion"] el valor que se añade
    notas_por_grupo.setdefault(grupo, []).append(a["programacion"])

print("Notas agrupadas: ", notas_por_grupo)


# calcular media de cada grupo
medias = {}

# .items() devuelve los pares del diccionario
for grupo, notas in notas_por_grupo.items():
    medias[grupo] = round(sum(notas) / len(notas), 2)

print("Media de programación por grupo:", medias)