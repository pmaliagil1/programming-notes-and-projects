numero = int(input("Introduce un número entero: "))
factorial = 1
resta = numero
if numero < 0:
    print("No se puede hacer el factorial de un número negativo")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    while resta > 0:
        factorial = factorial * resta
        resta = resta - 1
    print(f"El factorial de {numero} es {factorial}.")
