# MAIN - ejecucion de problemas

from problemas.problema1 import ejecutar_problema1
from problemas.problema2 import ejecutar_problema2
from problemas.problema3 import ejecutar_problema3


def main():
    while True:
        print("\nPARCIAL 2 - ADA")
        print("Seleccione una opción:")
        print("1. Hacer sencillo")
        print("2. Knapsack fraccionado")
        print("3. Teclado Nokia")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            ejecutar_problema1()

        elif opcion == "2":
            ejecutar_problema2()

        elif opcion == "3":
            ejecutar_problema3()

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opcion no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()