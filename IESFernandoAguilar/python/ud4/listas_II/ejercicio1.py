def matriz_diagonal(n):
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matriz[i][i] = 1
    
    return matriz

def imprime(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

n = 5
matriz = matriz_diagonal(n)
imprime(matriz)
