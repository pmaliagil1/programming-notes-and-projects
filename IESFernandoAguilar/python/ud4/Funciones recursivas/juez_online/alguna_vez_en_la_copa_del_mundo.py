def goles_argentina(goles):
    if len(goles) == 0:
        return 0
    return int(goles[0]) + goles_argentina(goles[1:])

if __name__ == "__main__":
    num_casos = int(input())
    resultados = []

    for _ in range(num_casos):
        goles = input()
        resultados.append(goles_argentina(goles))
    for resultado in resultados:
        print(resultado)
