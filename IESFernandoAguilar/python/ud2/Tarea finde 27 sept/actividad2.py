suma = 0
total = 0
numero = int(input("Introduce un número (0 para terminar): "))
while numero != 0:
    suma = suma + numero
    total = total + 1
    numero = int(input("Introduce un número (0 para terminar): "))
if total > 0:
    media = suma / total
    print(f"La suma de los números es: {suma}")
    print(f"La media de los números es: {media}")
else:
    print("No se introdujeron números para calcular la suma y la media.")



