# datos_ausentes.py

import json
import numpy as np
 
with open("notas.json", encoding="utf-8") as f:
    alumnos = json.load(f)


# numpy no adminte None en calculos, por lo que hay que convertirlo en NaN

fisica_con_none = [a["fisica"] for a in alumnos]
print("Lista con None: ", fisica_con_none)

arr_objeto = np.array(fisica_con_none)
print("Dtype con none: ", arr_objeto.dtype) # object no sirve para calcular

fisica = np.array([a["fisica"] if a["fisica"] is not None else np.nan for a in alumnos])
print("\nArray con NaN: ", fisica)
print("Dtype: ", fisica.dtype)  # loat64

# NaN contagia los calculos
print("\n--- Efecto de NaN ---")
print("mean() con NaN:", fisica.mean())
print("sum() con NaN:", fisica.sum())
print("max() con NaN:", fisica.max())


# -funciones que ignoran los NaN-
print("\n--- Funciones NaN ---")
print("nanmean: ", np.nanmean(fisica))  # numpy divide automaticamente entre los datos validos, no entre el total
print("nansum: ", np.nansum(fisica))
print("nanmax: ", np.nanmax(fisica))
print("nanmin: ", np.nanmin(fisica))


# -detectar y contar los datos ausentes-
# NaN no es igual a sí mismo (NaN == NaN da False), para detectarlo hay que usar np.isnan()
ausentes = np.isnan(fisica)
print("\n--- Detectar NaN ---")
print("Máscara de ausentes: ", ausentes)
print("Cuantos faltan: ", ausentes.sum())
print("Cuantos hay: ", (~ausentes).sum())

nombres = np.array([a["nombre"] for a in alumnos])
print("Falta nota de fisica: ", nombres[ausentes])

# para quedarnos unicamente con los datos validos
fisica_valida = fisica[~ausentes]
print("Notas válidas:", fisica_valida)
print("Media con datos válidos:", fisica_valida.mean())
