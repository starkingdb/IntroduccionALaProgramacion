import random

matriz = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]

print("Matriz 5x5:")
for fila in matriz:
    print(fila)

print("\nSuma de cada fila:")
for i, fila in enumerate(matriz):
    suma_fila = sum(fila)
    print(f"Suma de la fila {i+1}: {suma_fila}")

print("\nSuma de cada columna:")
for col in range(5):
    suma_columna = sum(matriz[fila][col] for fila in range(5))
    print(f"Suma de la columna {col+1}: {suma_columna}")
