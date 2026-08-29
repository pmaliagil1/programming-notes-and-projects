def contar_cifras(numero):
    if numero < 10:
        return 1
    return 1 + contar_cifras(numero // 10)

if __name__ == "__main__":
    num_casos = int(input())
    resultados = []

    for _ in range(num_casos):
        numero = int(input())
        resultados.append(contar_cifras(numero))

    for resultado in resultados:
        print(resultado)
