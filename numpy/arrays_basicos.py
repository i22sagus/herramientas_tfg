# arrays_basicos.py

import json
import numpy as np  # para abreviar a np

with open("notas.json", encoding="utf8") as f:
    alumnos = json.load(f)

# -pasar de lista de python a numpy-
lista_mates = [a["matematicas"] for a in alumnos]
print("Lista de python: ", lista_mates)
print("Tipo: ", type(lista_mates))

# np.array(lista) convierte la lista en un array de NumPy
mates = np.array(lista_mates)
print("\nArray de NumPy: ", mates)
print("Tipo: ", type(mates))

# un array tiene información sobre si mismo
print("Forma (Shape): ", mates.shape)
print("Tipo de dato (dtype): ", mates.dtype)
print("Número de elementos (size): ", mates.size)


# -estadisticas-
print("\n--- Estadisticas de matemáticas ---")
print("Suma: ", mates.sum())
print("Media: ", mates.mean())
print("Máximo: ", mates.max())
print("Mínimo: ", mates.min())

# se puede ver donde esta el máximo o el mínimo
# esto nos permite buscar el nombre del alumno en la lista original
posicion_max = mates.argmax()
print("Mejor alumno: ", alumnos[posicion_max]["nombre"])


# -operaciones sobre el array-
print("\n--- Operaciones sobre el array ---")
print("Notas + 0.5: ", mates + 0.5)
print("Notas * 10: ", mates * 10)
print("Notas / 10: ", mates / 10)

# se pueden hacer comparaciones a todo el array
aprobados = mates >= 5
print("Aprobados: ", aprobados)

print("Numero de aprobados: ", aprobados.sum())
print("Numero de suspensos: ", (~aprobados).sum())  # '~' invierte True/False


# -operaciones entre dos arrays-
# si los arrays tienen el mismo tamaño las operaciones se hacen posición a posición
prog = np.array([a["programacion"] for a in alumnos if a["programacion"] is not None])
print("Notas de programación (sin None): ", prog)

# por ejemplo, tenemos un array con notas 'bonus' que suman 0.5 si el alumno ha entregado un trabajo optativo
bonus = np.array([1, 0, 1, 0, 0, 0, 1, 0, 0, 0])
final = mates + bonus * 0.5
print("Mates + bonus: ", final)