"""Escribe un programa que solicite dos números por teclado y nos diga si son primos gemelos
o no. Dos números primos son gemelos cuando son primos, y además están separados por
dos unidades. Por ejemplo, 3 y 5, 11 y 13, etc."""

#REPASAR ESTE EJERCICIO

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3

    while i * i <= n:
        if n % i == 0:
            return False     
        i += 2
    return True

def primosGemelos(n1, n2):
    if not es_primo(n1) or not es_primo(n2):
        return False
    if n1 - n2 == 2 or n1 - n2 == -2:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        n1 = int(input("Introduce un primer número: "))
        n2 = int(input("Introduce un segundo número: "))

        if primosGemelos(n1, n2):
            print(f"Los números {n1} y {n2} SÍ son primos gemelos.")
        else:
            print(f"Los números {n1} y {n2} NO son primos gemelos.")
            
    except ValueError:
        print("Error: Por favor, introduce solo números enteros válidos.")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")