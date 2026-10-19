# indexado_y_filtros.py

import json
import numpy as np

with open("notas.json", encoding="utf8") as f:
    alumnos = json.load(f)


# convertir columnas en arrays
nombres = np.array([a["nombre"] for a in alumnos])
grupos = np.array([a["grupo"] for a in alumnos])
mates = np.array([a["matematicas"] for a in alumnos])

print("Nombres: ", nombres)
print("Mates: ", mates)


# -indices y slicing-
print("\n--- Indices y slicing ---")
print("Primer elemento: ", mates[0])
print("Ultimo elemento: ", mates[-1])   # -1 ultimo, -2 penultimo...
print("Los 3 primeros: ", mates[:3])    # del 0 al 2
print("Del 7 en adelante: ", mates[7:])
print("De 2 en 2: ", mates[::2])    # [inicio:fin:salto]


# -mascaras booleanas-
# una comparación sobre un array que produce otro array de True/False del mismo tamaño

print("\n--- Mascaras booleanas ---")
mascara = mates >= 7
print("Máscara (mates >= 7): ", mascara)

# si se usa la mascara como indice nos quedamos unicamente con las posiciones True
print("Notas >= 7: ", mates[mascara])

# como todos los arrays tienen el mismo orden, se puede utilizar la mascara para sacar los nombres de los alumnos con nota >= 7
print("Alumnos con > 7: ", nombres[mascara])
print("Alumnos suspensos < 5: ", nombres[mates < 5])


# -combinar condiciones-
# & "and", | "or", ~ "no"      las condiciones van entre ()

print("\n--- Combinar condiciones ---")
print("Grupo A con >= 7: ", nombres[(grupos == "A") & (mates >= 7)])
print("Mates < 5 o >= 9: ", nombres[(mates < 5) | (mates >= 9)])

# estadisticas por grupo (filtrar y calcular media)
print("\n--- Media de mates por grupo ---")
print("Grupo A: ", mates[grupos == "A"].mean())
print("Grupo B: ", mates[grupos == "B"].mean())


# -ordenacion-
print("\n--- Ordenacion ---")
print("Notas ordenadas: ", np.sort(mates))

# np.argsort no devuelve las notas ordenadas, devuelve las posiciones a seguir para ordenarlas
orden = np.argsort(mates)
print("Posiciones en orden ascendente: ", orden)
print("Nombres de menor a mayor nota: ", nombres[orden])

# [::-1] invierte un array: de esta forma obtenemos de mayor a menor
print("Top 3: ", nombres[orden[::-1][:3]])


# -np.where(condicion, valor_si_True, valor_si_False)-
estado = np.where(mates >= 5, "Aprobado", "Suspenso")
print("\n--- np.where ---")
for nombre, nota, est in zip(nombres, mates, estado):
    # zip() recorre varios arrays a la vez en paralelo
    print(f"{nombre:8s} {nota:5.1f} {est}")