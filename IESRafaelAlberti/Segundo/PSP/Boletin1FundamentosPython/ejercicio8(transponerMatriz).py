"""8. Matriz y Transposición: Representa una matriz de 3x3 usando listas anidadas.
Escribe una función que devuelva la matriz traspuesta (cambiar filas por
columnas)."""

def transponer(matriz):
    return [[fila[columna]for fila in matriz]for columna in range(3)]

if __name__ == "__main__":
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
print("Matriz original:")
for fila in matriz:
    print(fila)

print("Matriz traspuesta:")
for fila in transponer(matriz):
    print(fila)