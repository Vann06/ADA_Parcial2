# PARCIAL 2 - ANÁLISIS Y DISEÑO DE ALGORITMOS

Este repositorio contiene la implementación de los 3 problemas requeridos en el Examen Parcial 2 

Los problemas implementados son:

1. Hacer sencillo
2. Knapsack fraccionado
3. Teclado Nokia

---

## Video de explicación

[![Explicación del Parcial 2](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=VIDEO_ID)

> Reemplazar `VIDEO_ID` por el ID real del video subido a YouTube como no listado.

---

## Descripción de los problemas

### Problema 1: Hacer sencillo

Dado un monto `m`, se busca formar dicho monto utilizando la menor cantidad posible de monedas.

Las denominaciones disponibles son:

- 1
- 5
- 10
- 25

El algoritmo utiliza un enfoque **greedy**, seleccionando siempre la moneda de mayor denominación posible.

---

### Problema 2: Knapsack fraccionado

Se tiene una mochila con capacidad máxima `W` y una lista de artículos, donde cada artículo posee:

- precio
- peso

Como el problema permite tomar fracciones de los artículos, se utiliza un enfoque **greedy**, ordenando los artículos según su valor por unidad:

```text
valor_unitario = precio / peso
```

Luego se toman primero los artículos con mayor valor unitario hasta llenar la mochila.

---

### Problema 3: Teclado Nokia

Dado un número entero positivo `n`, se desea contar la cantidad total de combinaciones de `n` dígitos que pueden formarse usando el teclado Nokia.

Restricciones:

- Se puede iniciar en cualquier dígito.
- El siguiente teclazo debe ser un vecino válido: arriba, abajo, izquierda, derecha o la misma tecla.
- No se permite presionar `*` ni `#`.

Este problema se resuelve mediante **programación dinámica con memoización**, utilizando estados de la forma:

```text
(longitud, tecla)
```

Además, para mostrar las combinaciones generadas, se utiliza una función de backtracking que construye las cadenas válidas.

---


## Arquitectura del código

El código se organizó de forma modular, separando cada problema en su propio archivo y utilizando un archivo `main.py` para ejecutar el menú principal.

```text
ADA_Parcial2/
├── main.py
├── Problemas/
│   ├── __init__.py
│   ├── problema1.py
│   ├── problema2.py
│   └── problema3.py
├── docs/
│   └── parcial2_ejercicios.pdf
├── README.md
└── .gitignore
```

---

## Ejecución del programa

Para ejecutar el proyecto, usar el siguiente comando desde la carpeta principal:

```bash
python main.py
```

El programa mostrará un menú con las siguientes opciones:

```text
1. Hacer sencillo
2. Knapsack fraccionado
3. Teclado Nokia
0. Salir
```

---

## Casos de prueba

Cada problema incluye al menos tres casos de prueba no triviales.

### Problema 1

Ejemplos de montos:

```text
293 centavos
87 centavos
141 centavos
```

### Problema 2

Ejemplos de capacidades:

```text
W = 50
W = 15
W = 60
```

Cada caso utiliza artículos con precio y peso. El algoritmo muestra qué artículo se seleccionó, cuánta cantidad se tomó y qué valor se obtuvo.

### Problema 3

Ejemplos de longitud:

```text
n = 1
n = 2
n = 3
```

Para `n = 2`, el resultado esperado es 36 combinaciones.

---

## Tecnologías utilizadas

- Python 3
- Programación modular
- Algoritmos greedy
- Programación dinámica con memoización
- Backtracking para mostrar combinaciones generadas

---

## Estructura general de ejecución

El archivo `main.py` importa las funciones principales de cada problema:

```python
from Problemas.problema1 import ejecutar_problema1
from Problemas.problema2 import ejecutar_problema2
from Problemas.problema3 import ejecutar_problema3
```

Cada archivo contiene:

- una función con la lógica principal del algoritmo
- una función `ejecutar_problemaX()` que permite correr el problema desde el menú principal

---

