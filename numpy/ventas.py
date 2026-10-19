# ventas.py

import json
import numpy as np

with open("ventas.json", encoding="utf-8") as f:
    datos = json.load(f)
ventas = datos["ventas"]

# - pasar los datos a arrays -
# Convertimos cada campo que necesitamos en un array. Todos tienen 40 elementos
# estan en el mismo orden: la posición i de cada array es la venta i.
unidades = np.array([v["unidades"] for v in ventas])
precios = np.array([v["precio_unitario"] for v in ventas])
productos = np.array([v["producto"] for v in ventas])
categorias = np.array([v["categoria"] for v in ventas])
meses = np.array([v["fecha"][:7] for v in ventas])

print("Ventas:", len(ventas))
print("Primeras 5 unidades:", unidades[:5])
print("Primeros 5 precios: ", precios[:5])


# - ingreso de cada venta y total -
ingresos = unidades * precios
print("\nIngresos de las 5 primeras ventas:", ingresos[:5])
print("Ingreso total:", ingresos.sum())  


# - agrupar con máscaras -
# np.unique(array) devuelve los valores distintos, ordenados alfabéticamente.
print("\n--- Ingreso por categoría ---")
for cat in np.unique(categorias):
    # 'categorias == cat' es una máscara True donde la categoría coincide.
    # Aplicada a 'ingresos', deja solo los ingresos de esa categoría.
    total_cat = ingresos[categorias == cat].sum()
    print(f"{cat:12s} {total_cat:>8}")

print("\n--- Unidades por producto ---")
unidades_producto = {}
for prod in np.unique(productos):
    unidades_producto[prod] = int(unidades[productos == prod].sum())
    print(f"{prod:12s} {unidades_producto[prod]:>4}")

print("Más vendido:", max(unidades_producto, key=unidades_producto.get))


# - comprobación de coherencia -

suma_categorias = sum(ingresos[categorias == c].sum() for c in np.unique(categorias))
print("\nSuma de categorías:", suma_categorias, "| Total:", ingresos.sum())
print("¿Coinciden?", suma_categorias == ingresos.sum())
# np.isclose compara números decimales con tolerancia. aquí son enteros, pero es la forma segura de comparar decimales.


# - evolución mensual, acumulados y variaciones -

lista_meses = np.unique(meses)                       # ya vienen ordenados
ingresos_mes = np.array([ingresos[meses == m].sum() for m in lista_meses])

print("\n--- Ingresos por mes ---")
for m, i in zip(lista_meses, ingresos_mes):
    print(f"{m}: {i:>6}")

# np.cumsum: suma acumulada. Cada elemento = suma de todos los anteriores + él.
# Sirve para ver cuánto llevamos vendido a lo largo del año.
print("\nAcumulado:", np.cumsum(ingresos_mes))

# np.diff: diferencia entre cada elemento y el anterior. Muestra cómo cambian
# los ingresos de un mes al siguiente (positivo = subió, negativo = bajó).
variacion = np.diff(ingresos_mes)
print("Variación mes a mes:", variacion)
print("Mayor caída:", lista_meses[1:][variacion.argmin()], "(", variacion.min(), ")")
# lista_meses[1:] porque diff devuelve un elemento MENOS (compara pares).

# Cuota de cada mes sobre el total, en porcentaje:
porcentajes = ingresos_mes / ingresos_mes.sum() * 100
print("\n% del total por mes:", porcentajes.round(1))
print("Suma de porcentajes:", porcentajes.sum().round(1))