#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablaMultiplicar(n):
    resultado=""
    for i in range(1,11):
        multiplicacion = n*(i)
        resultado = resultado+","+str(multiplicacion)
    print(resultado[1:])

if __name__ == "__main__":
    try:
        n = int(input("Escribe la tabla de multiplicar hasta 10 que quieras ver: "))
        tablaMultiplicar(n)
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Error desconodico {e}")