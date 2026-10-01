def calcular_factorial(n):

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    numero = int(input("Introduce un número para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        resultado = calcular_factorial(numero)
        print(f"El factorial de {numero} es {resultado}.")
