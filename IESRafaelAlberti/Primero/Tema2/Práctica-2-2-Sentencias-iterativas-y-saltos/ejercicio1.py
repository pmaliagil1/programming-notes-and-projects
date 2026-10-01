# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

def pintaNumero(n):
    resultado = (n+", ")*10
    print(resultado[:-2])

if __name__ == "__main__":
    n = input("Introduce un número: ")

    pintaNumero(n)