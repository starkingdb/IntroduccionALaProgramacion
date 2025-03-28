vector_cadenas = []

for i in range(5):
    valor = input(f"Ingrese el valor {i+1}: ")
    vector_cadenas.append(valor)

vector_invertido = vector_cadenas[::-1]

print("Vector invertido:")
for cadena in vector_invertido:
    print(cadena)
