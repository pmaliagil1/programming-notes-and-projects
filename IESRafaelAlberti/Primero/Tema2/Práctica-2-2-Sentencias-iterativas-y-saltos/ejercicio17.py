#Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo
#componen.

def sumaDigitos(n):
    if n >=0:
        suma = 0
        cadena = str(n)
        for numero in cadena:
            suma += int(numero)
        return suma
    else:
        raise NameError("NUMERO NEGATIVO")

if __name__ == "__main__":
    try:
        n = int(input("Introduce un entero positivo: "))
        print(sumaDigitos(n))
    except ValueError:
        print("Valor no válido")
    except NameError:
        print("El número debe ser positivo")
    except Exception as e:
        print(f"Error desconocido: {e}")
