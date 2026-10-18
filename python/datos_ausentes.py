# datos_ausentes.py
# Este programa interpreta ficheros con datos ausentes

import json
 
with open("notas.json", encoding="utf-8") as f:
    alumnos = json.load(f)

print("Elena ->", alumnos[4]["nombre"], alumnos[4]["fisica"])

try:
    suma = 0
    for a in alumnos:
        # Cuando llegue a Elena, intentará hacer 6.5 + None, que no tiene
        # sentido matemático. Python lanza un TypeError.
        suma += a["fisica"]
except TypeError as error:
    # 'error' contiene el mensaje del problema. No se puede
    # sumar un 'float' con un 'NoneType' (el tipo de None).
    print("ERROR al sumar sin filtrar:", error)

# Para solucionar este problema tenemos que ignorar los None
suma = 0
validos = 0

for a in alumnos:
    if a["fisica"] is not None:
        suma+=a["fisica"]
        validos+=1

mediaFisica=suma/validos
print(f"Media física: {mediaFisica:.2f} (calculada con {validos} de {len(alumnos)}) validos")

# Utilizando list comprehension
notas_fisica = [a["fisica"] for a in alumnos if a["fisica"] is not None]
print("Versión corta:", round(sum(notas_fisica) / len(notas_fisica), 2))