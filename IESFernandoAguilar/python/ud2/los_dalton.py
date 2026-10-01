while True:
    n = int(input("Introduce el número de personas en la viñeta: "))
    if n == 0:
        break
    alturas = list(map(int, input("Introduce las alturas de las personas: ").split()))
    if alturas == sorted(alturas) or alturas == sorted(alturas, reverse=True):
        print("DALTON")
    else:
        print("DESCONOCIDOS")
