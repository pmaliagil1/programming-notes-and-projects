n = 1
negativos = []
positivos = []
while n != 0:
    n = int(input("Escribe un numero (0 para terminar): "))
    if n > 0:
        positivos.append(n)
    elif n<0:
        negativos.append(n)
print(f"Positivos: {positivos} \nNegativos: {negativos}")