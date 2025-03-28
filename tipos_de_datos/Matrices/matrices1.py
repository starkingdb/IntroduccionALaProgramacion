matriz = [[1, 2], [3, 4]]

suma_elementos = sum(sum(fila) for fila in matriz)
promedio = suma_elementos / (len(matriz) * len(matriz[0]))
print(f"El promedio de los elementos de la matriz es: {promedio}")
