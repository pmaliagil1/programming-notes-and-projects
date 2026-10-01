"""""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el 
usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares 
tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en 
total."""

def parImpar():
    n = -1
    par = 0
    impar = 0
    while n != 0:
        try:
            n = int(input("Introduce un entero positivo (0 para terminar): "))
            if n % 2 == 0:
                par += 1
            elif n % 2 != 0:
                impar += 1
        except ValueError:
            print("Valor no válido")
    print(f"CONTADOR\nPar: {par - 1}\nImpar: {impar}")



if __name__ == "__main__":
    try:
        parImpar()
    except Exception as e:
        print(f"Algo ha salido mal: {e}")