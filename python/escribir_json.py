# escribir_json.py
# este programa lee, procesa y escribe ficheros json

import json

# -leer json-
with open("ventas.json", encoding="utf8") as f:
    datos = json.load(f)

ventas = datos["ventas"]

# -procesar datos-
ingreso_total = 0
por_categoria = {}
unidades_por_producto = {}
ingresos_por_mes = {}

for v in ventas:
    ingreso = v["unidades"] * v["precio_unitario"]
    ingreso_total += ingreso

    por_categoria[v["categoria"]] = por_categoria.get(v["categoria"], 0) + ingreso
    unidades_por_producto[v["producto"]] = unidades_por_producto.get(v["producto"], 0) + v["unidades"]
    mes = v["fecha"][:7]
    ingresos_por_mes[mes] = ingresos_por_mes.get(mes, 0) + ingreso

mas_vendido = max(unidades_por_producto, key=unidades_por_producto.get)
mejor_mes = max(ingresos_por_mes, key=ingresos_por_mes.get)

# reunir todos los datos en un unico diccionario

resumen = {
    "tienda": datos["tienda"],
    "moneda": datos["moneda"],
    "numero_ventas": len(ventas),
    "ingreso_total": ingreso_total,
    "ingreso_por_categoria": por_categoria,
    "unidades_por_producto": unidades_por_producto,
    "ingresos_por_mes": dict(sorted(ingresos_por_mes.items())),
    "producto_mas_vendido": mas_vendido,
    "mes_con_mas_ingresos": mejor_mes,
}

# -escribir resumen en un nuevo archivo-
# abrimos el archivo en modo escritura, si no existe se crea
with open("resumen.json", "w", encoding="utf-8") as f:
    # json.dump(datos, archivo, opciones)
    # ensure_ascii = conserva tildes y ñ
    # indent=2 hace el archivo legible añadiendo saltos de linea y sangrias
    json.dump(resumen, f, ensure_ascii=False, indent=2)

print("Archivo resumen.json creado. Contenido:")
print()

# -comprobacion-
with open("resumen.json", encoding="utf-8") as f:
    print(f.read())
