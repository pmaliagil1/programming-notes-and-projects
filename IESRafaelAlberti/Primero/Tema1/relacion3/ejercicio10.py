notas = 0
contador = 0
while notas != -1:
    notas = int(input("Escribe una nota (-1 para terminar): "))
    if notas == 10:
        print("La nota es un 10")
        contador += 1
    elif notas == -1:
        break
    else:
        continue

print(f"El total de notas que son un 10 son: {contador}")