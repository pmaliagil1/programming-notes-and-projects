"""Diseña un algoritmo en el que se solicite un número por teclado y nos diga si es múltiplo de
2, de 3, de ambos o de ninguno. Por ejemplo, 6 es múltiplo de 2 y de 3; 4 es múltiplo de 2, 9
es múltiplo de 3 y 5 no es múltiplo de ninguno."""

def multiplo(n):
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} es multiplo de 2 y 3")
    elif n %2 == 0 and n %3 != 0:
        print(f"{n} es multiplo de 2 pero no de 3")
    elif n%2 !=0 and n%3 == 0:
        print(f"{n} no es multiplo de 2 pero si de 3")
    elif n%2 != 0 and n%3 !=0:
        print(f"{n} no es multiplo ni de 2 ni de 3")
    else:
        raise NameError("ERROR DESCONOCIDO")


if __name__ == "__main__":
    try:
        n = int(input("Introduce un número: "))
        multiplo(n)


    except ValueError:
        print("Valor no válido")
    except NameError:
        print("Error desconocido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")