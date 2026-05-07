# PROBLEMA 3. NOKIA PROBLEM

# para este tenemos un telefono con una pantalla de 4x4 y un teclado con los numeros del 0 al 9, * y #
# Se desea contar el total de combinaciones de n digitos que existen con respecto a :

# 1. podemos comenzar con cualquier numero
# 2. El siguiente teclazo debe ser un vecino arriba, abajo, izquierda o derecha del anterior
# 3. Se ignoran * y #

# Lista de vecinos para cada numero en el teclado
vecinos = {
    '0': ['0','8'],
    '1': ['1','2', '4'],
    '2': ['2','1', '3', '5'],
    '3': ['3', '2', '6'],
    '4': ['4', '1', '5', '7'],
    '5': ['5', '2', '4', '6', '8'],
    '6': ['6', '3', '5', '9'],
    '7': ['7', '4', '8'],
    '8': ['8', '5', '7', '9', '0'],
    '9': ['9', '6', '8']
}

def contar_combinaciones(n):
    memo = {}

    def dp(longitud, ultimo):
        if longitud == 1:
            return 1
        if (longitud, ultimo) in memo:
            return memo[(longitud, ultimo)]
        total = 0
        for vecino in vecinos[ultimo]:
            total += dp(longitud - 1, vecino)
        memo[(longitud, ultimo)] = total
        return total
    total_combinaciones = 0
    for tecla in range(10):
        total_combinaciones += dp(n, str(tecla))
    return total_combinaciones

n = int(input("Ingrese la longitud de la combinación (n): "))
total_combinaciones = contar_combinaciones(n)
print(f"Total de combinaciones de {n} dígitos: {total_combinaciones}")
