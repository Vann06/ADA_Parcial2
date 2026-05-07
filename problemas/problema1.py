# PROBLEMA 1. HACER SENCILLO 

# Problema dado un monto m buscamos analizar dicho monto con la 
# menor cantidad posible de monedas 
# Las monedas disponibles son: 1, 5, 10, 25
# Se pueden tomar todas las monedas que necesitemos de cada denominación

def main():
    m = int(input("Ingrese el monto a analizar: "))

monedas = [25, 10, 5, 1]
resultado = {}
total_monedas = 0 

for moneda in monedas:
    cantidad_monedas = m // moneda
    resultado[moneda] = cantidad_monedas
    total_monedas += cantidad_monedas
    m -= cantidad_monedas * moneda

print("Cantidad de monedas necesarias:")
for moneda, cantidad in resultado.items():
    print(f"{moneda} centavos: {cantidad}")
    print(f"Total de monedas utilizadas: {total_monedas}")

print("=" * 30)


