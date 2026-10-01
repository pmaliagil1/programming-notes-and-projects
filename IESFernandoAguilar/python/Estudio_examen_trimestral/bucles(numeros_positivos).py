total_numeros = int(input())
contador = 0
positivos = 0
negativos = 0
while contador < total_numeros:
    numero = int(input())
    contador += 1
    if numero > 0:
        positivos += 1
print(f"{positivos}")