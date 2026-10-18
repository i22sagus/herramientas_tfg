# leer_json.py
# Este programa lee el archivo alumno.json e imprime su contenido

import json

with open("alumno.json", encoding="utf8") as f:
    datos = json.load(f)

# json con { } se convierte en un diccionario
print("Tipo de 'datos':", type(datos))

# acceder a un valor del diccionario
print("Nombre: ", datos["nombre"])
print("Edad: ", datos["edad"])

# acceso a los datos de una lista
print("Primera asignatura: ", datos["asignaturas"][0])
print("Segunda asignatura: ", datos["asignaturas"][1])
print("Tercera asignatura: ", datos["asignaturas"][2])
print("Todas las asignaturas: ", datos["asignaturas"], type(datos["asignaturas"]))

# imprimir un diccionario de dentro de otro diccionario
print("Email:", datos["contacto"]["email"])

# imprimir true/false 
print("¿Activo?", datos["activo"])