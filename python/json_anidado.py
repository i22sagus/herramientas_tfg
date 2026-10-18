# json_anidado.py
# este programa saca los resultados de las ventas de una tienda

import json

with open("ventas.json", encoding="utf8") as f:
    datos = json.load(f)

print("Tienda: ", datos["tienda"], "| Moneda: ", datos["moneda"])

ventas = datos["ventas"]
print("Numero de ventas: ", len(ventas))

print("Ejemplo de venta: ", ventas[0])

# -ingreso total-
total = 0
for v in ventas:
    total += v["unidades"] * v["precio_unitario"]

print(f"Ingreso total: {total} {datos['moneda']}")

# -ingreso por categoria-
por_categoria = {}

for v in ventas:
    ingreso = v["unidades"] * v["precio_unitario"]

    # si pedimos por_categoria["Audio"] obtenemos KeyError
    # se soluciona usando .get(clave, 0) que devuelve el valor de la clave si existe,
    # devuelve 0 si no existe.
    # así la primera vez suma 0 + ingreso, y las siguientes veces suma lo acumulado
    por_categoria[v["categoria"]] = por_categoria.get(v["categoria"], 0) + ingreso

print("Ingreso por categoría: ", por_categoria)

# -producto mas vendido en unidades-
unidades_por_producto = {}

for v in ventas:
    unidades_por_producto[v["producto"]] = unidades_por_producto.get(v["producto"], 0) + v["unidades"]

print("Unidades por producto: ", unidades_por_producto)

# key=unidades_por_producto.get mira cuantas unidades tiene cada producto
mas_vendido = max(unidades_por_producto, key=unidades_por_producto.get)
print(f"Más vendido: {mas_vendido} ({unidades_por_producto[mas_vendido]} unidades)")

# -mes con mas ingresos-
ingresos_por_mes = {}

# para agrupar solo necesitamos una parte de la fecha ("2026-03") por lo que utilizamos slicing
# texto[inicio:fin] devuelve un trozo del texto
for v in ventas:
    mes = v["fecha"][:7]
    ingresos_por_mes[mes] = ingresos_por_mes.get(mes, 0) + v["unidades"] * v["precio_unitario"]

# sorted(diccionario) devuelve las claves ordenadas de menor a mayor
# los meses tienen el formato año-mes, por lo que usamos el orden de los meses

for mes in sorted(ingresos_por_mes):
    print(f" {mes}: {ingresos_por_mes[mes]}")

mejor_mes = max(ingresos_por_mes, key=ingresos_por_mes.get)
print(f"Mes con más ingresos: {mejor_mes} ({ingresos_por_mes[mejor_mes]} {datos['moneda']})")