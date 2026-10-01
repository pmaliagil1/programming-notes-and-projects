def es_ganador(digitos_extraidos, boleto):
    contador_extraidos = [0] * 10
    contador_boleto = [0] * 10

    for digito in digitos_extraidos:
        contador_extraidos[int(digito)] += 1

    for digito in boleto:
        contador_boleto[int(digito)] += 1

    for i in range(10):
        if contador_boleto[i] > contador_extraidos[i]:
            return False
    return True

n = int(input())
resultados = []

for _ in range(n):
    digitos_extraidos, boleto = input().split()
    if es_ganador(digitos_extraidos, boleto):
        resultados.append("GANA")
    else:
        resultados.append("PIERDE")

for resultado in resultados:
    print(resultado)
