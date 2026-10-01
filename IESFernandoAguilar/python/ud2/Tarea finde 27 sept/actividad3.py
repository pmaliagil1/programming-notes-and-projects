cantidad = int(input("Introduce la cantidad de números que va a escribir: "))
mayores = 0
menores = 0
cero = 0
contador = 0
while contador < cantidad:
    numero = float(input("Introduce un número: "))
    if numero > 0:
        mayores = mayores + 1
    elif numero < 0:
        menores = menores + 1
    else:
        cero = cero + 1
    contador = contador +1
print(f"Hay un total de {mayores} números mayores que 0")
print(f"Hay un total de {menores} números menores que 0")
print(f"Hay un total de {cero} números iguales que 0")
