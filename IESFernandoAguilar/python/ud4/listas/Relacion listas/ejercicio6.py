def pares(lista):
    return [x for x in lista if x % 2 == 0]

entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
salida = pares(entrada)

print("Entrada:", entrada)
print("Salida (valores pares):", salida)
