"""Dibuja un ordinograma de un programa que calcule el valor A elevado a B
(A^B) sin hacer uso del operador de potencia (^), siendo A y B valores
introducidos por teclado, y luego muestre el resultado por pantalla."""

def calculaPotencia(n1,n2):
    potencia = n1
    for i in range(n2-1):
        potencia = potencia*n1
    return f"El resultado es: {potencia}"
if __name__ == "__main__":
    try:
        n1 = int(input("Introduce el numero que quieres elevar: "))
        n2 = int(input("Introduce la potenecia a la que quieres elevar el número ya introducido: "))
        print(calculaPotencia(n1,n2))
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")