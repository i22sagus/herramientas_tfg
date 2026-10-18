# recorrer_lista.py
# Este programa recorre los datos de una lista que se encuentra en notas.json (lista de diccionarios)

import json

with open("notas.json", encoding="utf8") as f:
    datos=json.load(f)

print("Numero de alumnos:", len(datos))

for alumno in datos:
    # f es un "f-string", es decir, lo que va entre { } se sustituye por su valor
    print(f"{alumno['nombre']} (grupo {alumno['grupo']}): matemáticas {alumno['matematicas']}, programación {alumno['programacion']}, física {alumno['fisica']}")
