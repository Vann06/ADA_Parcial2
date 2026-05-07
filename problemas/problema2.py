# PROBLEMA 2. KNAPSACK PROBLEM FRACCIONADO 


# Para este problema tenemos un ladron con una mochila que aguanta W unidades u de peso 
# Busca robar el maximo valor que pueda de una selección de n artículos 
# articulo i tiene precio p y hay w unidades de peso disponibles del mismo 

# No es necesario robar el articulo completo, se puede robar una fracción del mismo


# creación de casos de prueba rapiditos 
casos = [

    {
        "W": 50,
        "articulos": [
            (60, 10),  # precio, peso
            (150, 20),
            (90, 30)
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
        "W": 150,
        "articulos": [
            (200, 40),
            (150, 30),
            (300, 50)
        ]
    }
]

def knapsack_fraccionado(W, articulos):
    # Ordenamiento de artículos por valir por unidad
    for articulo in articulos:
        valor_unitario = articulo[0] / articulo[1]
        print(f"Artículo con precio {articulo[0]} y peso {articulo[1]} tiene valor por unidad: {valor_unitario}")

    # Ordenar artículos por valor por unidad en orden descendente
    articulos.sort(key=lambda x: x[0] / x[1], reverse=True)

    capacidad_restante = w
    valor_total = 0
    seleccion = []

    for articulo in articulos:
        if capacidad_restante == 0:
            break 
        cantidad_tomada = min(articulo[1], capacidad_restante)
        valor_obtenido = cantidad_tomada * (articulo[0] / articulo[1])

        valor_total += valor_obtenido
        seleccion.append({
            "articulo" : articulo,
            "cantidad_tomada" : cantidad_tomada,
            "valor_obtenido" : valor_obtenido
        })

        capacidad_restante -= cantidad_tomada

    print(f"Valor total obtenido: {valor_total}")
    print("Selección de artículos:")

for i, caso in enumerate(casos, start=1):
    print(f"\nCaso de prueba {i + 1}:")
    W = caso["W"]
    articulos = caso["articulos"]
    knapsack_fraccionado(W, articulos)