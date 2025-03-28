import random

vector_numeros = [random.randint(1, 10) for _ in range(10)]

for numero in vector_numeros:
    cuadrado = numero ** 2
    cubo = numero ** 3
    print(f"Numero: {numero}, Cuadrado: {cuadrado}, Cubo: {cubo}")
