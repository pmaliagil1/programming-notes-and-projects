def bolos_por_fila(n):
    if n == 1:
        return 1
    return n + bolos_por_fila(n - 1)

if __name__ == "__main__":

    num_casos = int(input())
    resultados = []

    for _ in range(num_casos):
        filas = int(input())
        resultados.append(bolos_por_fila(filas))
    for res in resultados:
        print(res)