# PROBLEMA 2. KNAPSACK PROBLEM FRACCIONADO 

# Para este problema tenemos un ladrón con una mochila que aguanta W unidades de peso.
# Busca robar el máximo valor que pueda de una selección de artículos.
# Cada artículo tiene precio y peso.
# No es necesario robar el artículo completo, se puede robar una fracción del mismo.


def knapsack_fraccionado(W, articulos):
    # Guardamos el número original del artículo para que sea más fácil leer la salida
    articulos_con_indice = []

    for i, articulo in enumerate(articulos, start=1):
        precio = articulo[0]
        peso = articulo[1]
        valor_unitario = precio / peso

        articulos_con_indice.append((i, precio, peso, valor_unitario))

    # Ordenamos por valor por unidad de mayor a menor
    articulos_ordenados = sorted(
        articulos_con_indice,
        key=lambda x: x[3],
        reverse=True
    )

    capacidad_restante = W
    valor_total = 0
    seleccion = []

    for articulo in articulos_ordenados:
        numero_articulo = articulo[0]
        precio = articulo[1]
        peso = articulo[2]
        valor_unitario = articulo[3]

        if capacidad_restante == 0:
            break

        cantidad_tomada = min(peso, capacidad_restante)
        valor_obtenido = cantidad_tomada * valor_unitario

        seleccion.append({
            "numero_articulo": numero_articulo,
            "precio": precio,
            "peso": peso,
            "cantidad_tomada": cantidad_tomada,
            "valor_unitario": valor_unitario,
            "valor_obtenido": valor_obtenido
        })

        valor_total += valor_obtenido
        capacidad_restante -= cantidad_tomada

    return seleccion, valor_total


def ejecutar_problema2():
    print("\nPROBLEMA 2: KNAPSACK FRACCIONADO")

    casos = [
        {
            "W": 50,
            "articulos": [
                (60, 10),   # precio, peso
                (100, 20),
                (120, 30)
            ]
        },
        {
            "W": 15,
            "articulos": [
                (30, 5),
                (40, 10),
                (45, 15)
            ]
        },
        {
            "W": 60,
            "articulos": [
                (200, 50),
                (150, 25),
                (180, 30)
            ]
        }
    ]

    for i, caso in enumerate(casos, start=1):
        W = caso["W"]
        articulos = caso["articulos"]

        print(f"\nCASO DE PRUEBA {i}")
        print(f"Capacidad de la mochila: {W} unidades")
        print("\nArtículos disponibles:")

        for j, articulo in enumerate(articulos, start=1):
            precio = articulo[0]
            peso = articulo[1]
            valor_unitario = precio / peso

            print(
                f"Artículo {j}: precio = {precio}, "
                f"peso = {peso}, "
                f"valor por unidad = {valor_unitario:.2f}"
            )

        seleccion, valor_total = knapsack_fraccionado(W, articulos)

        print("\nSelección realizada por el algoritmo greedy:")

        for item in seleccion:
            if item["cantidad_tomada"] == item["peso"]:
                tipo_toma = "se tomó completo"
            else:
                tipo_toma = "se tomó parcialmente"

            print(
                f"Se seleccionó el Artículo {item['numero_articulo']}: "
                f"{tipo_toma}. "
                f"Cantidad tomada = {item['cantidad_tomada']} de {item['peso']} unidades. "
                f"Valor obtenido = {item['valor_obtenido']:.2f}."
            )

        print(f"\nValor total máximo obtenido: {valor_total:.2f}")
