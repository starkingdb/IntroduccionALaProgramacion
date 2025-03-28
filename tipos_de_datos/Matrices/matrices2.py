matriz = [[1, 2, 3], [4, 5, 6]]

matriz_transpuesta = list(zip(*matriz))
print("La matriz transpuesta es:")
for fila in matriz_transpuesta:
    print(fila)

