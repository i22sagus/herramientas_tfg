# estadistica_descriptiva.py
# metodos estadísticos

import json
import numpy as np
 
with open("notas.json", encoding="utf-8") as f:
    alumnos = json.load(f)
 
mates = np.array([a["matematicas"] for a in alumnos])


# -medidas de tendencia central y dispersion-
print("Notas de mates: ", np.sort(mates))

# MEDIA
print("Media: ", np.mean(mates))

# MEDIANA: valor centro al ordenar los datos
print("Mediana: ", np.median(mates))

# DESVIACIÓN TÍPICA: cuanto se alejan, en promedio, los datos de la media
# Pequeña = datos muy parecidos entre sí. Grande = datos muy dispersos.
# NumPy calcula por defecto la desviación poblacional (divide entre n)
# para la muestral (divide entre n-1), hay que añadir ddof=1
print("Desviación típica (poblacional):", np.std(mates))
print("Desviación típica (muestral, ddof=1):", np.std(mates, ddof=1))

# VARIANZA: desviación tipica al cuadrado
print("Varianza (poblacional): ", np.var(mates))

# RANGO: diferencia entre el máximo y el mínimo, np.ptp lo calcula directamente
print("Rango: ", np.ptp(mates), "=", mates.max(), "-", mates.min())


# -percentiles-
# p valor por debajo del cual esta el p% de los datos
# percentil 50 = mediana;  25 y 75 = primer y tercer cuartil
print("\n--- Percentiles ---")
print("Percentil 25:", np.percentile(mates, 25))
print("Percentil 50:", np.percentile(mates, 50), "(= la mediana)")
print("Percentil 75:", np.percentile(mates, 75))

# tambien se pueden pedir varios percentiles a la vez
print("Percentiles 10, 50, 90:", np.percentile(mates, [10, 50, 90]))


# -arrays de 2 dimensiones (matrices)-
# para evitar los None solo voy a usar los alumnos que tienen las 3 notas
completos = [a for a in alumnos if a["programacion"] is not None and a["fisica"] is not None]
nombres = [a["nombre"] for a in completos]

tabla = np.array([[a["matematicas"], a["programacion"], a["fisica"]] for a in completos])
print("\n--- Array 2D ---")
print("Alumnos completos: ", nombres)
print("Forma: ", tabla.shape, "-> (filas, columnas)")
print(tabla)

# acceso a la tabla
print("Nota de la fila 0, columna 1:", tabla[0, 1])
print("Columna 0 entera (mates):", tabla[:, 0])    # ':' significa "todas las filas"
print("Fila 2 entera:", tabla[2, :])

# calculos en matrices
# axis: indica en que dirección se calcula
# axis = 0: calcula hacia abajo (un resultado por columna)
# axis = 1: calcula hacia el lado (un resultado por fila)
print("\nMedia por asignatura (axis=0):", tabla.mean(axis=0).round(2))
print("   (orden: matemáticas, programación, física)")
print("Media por alumno (axis=1):", tabla.mean(axis=1).round(2))
print("   (orden:", nombres, ")")


# -correlacion entre variables-
# mide si dos variables suben juntas. va de -1 a 1
# 1: relación directa 
# 0: sin relación lineal
# -1: relación inversa
mates_c = tabla[:, 0]
prog_c = tabla[:, 1]
fisica_c = tabla[:, 2]


# np.corrcoef devuelve una matriz 2x2 con todas las correlaciones 
matriz = np.corrcoef(mates_c, prog_c)
print("\n--- Correlación ---")
print("Matriz completa:\n", matriz.round(3))
print("Correlación mates-programación:", round(matriz[0, 1], 3))
print("Correlación mates-física:", round(np.corrcoef(mates_c, fisica_c)[0, 1], 3))

# correlación entre todas las asignaturas a la vez: rowvar=False, indica que las variables están en las columnas
print("\nMatriz de correlación (mates, prog, física):")
print(np.corrcoef(tabla, rowvar=False).round(3))
