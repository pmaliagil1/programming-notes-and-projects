#Muestra la tabla de multiplicar de un número introducido por teclado.

def tablaMultiplicar(n):
    for i in range(1,11):
        print(n*i)

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número: "))
        tablaMultiplicar(n)

    except ValueError:
        print("Entrada no válida")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
