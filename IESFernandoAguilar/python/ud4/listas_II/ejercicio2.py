def matriz_marco(n, m):
    matriz = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        matriz[i][0] = 1
        matriz[i][m - 1] = 1
    
    for j in range(m):
        matriz[0][j] = 1
        matriz[n - 1][j] = 1
    
    return matriz

def imprime(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

n = 5
m = 7
matriz = matriz_marco(n, m)
imprime(matriz)
