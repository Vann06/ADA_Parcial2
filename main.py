# MAIN - Manejo de problemas

# Importar los problemas
from problemas import problema1
from problemas import problema2
from problemas import problema3



def main():
    print("Bienvenido al programa de análisis de montos con monedas.")
    print("Selecciona el problema que deseas resolver:")
    print("1. Análisis de monto con monedas")
    
    opcion = input("Ingrese el número del problema a resolver: ")
    
    if opcion == '1':
        problema1
    elif opcion == '2':
        problema2
    elif opcion == '3':
        problema3
    else:
        print("Opción no válida. Por favor, selecciona un número válido.")