partidos = 0
entradas = int(input())
while partidos < entradas:
    goles1,goles2 = map(int,input().split())
    partidos += 1
    if goles1 > goles2:
        print("1")
    elif goles2 > goles1:
        print("2")
    elif goles1 == goles2:
        print("X")
