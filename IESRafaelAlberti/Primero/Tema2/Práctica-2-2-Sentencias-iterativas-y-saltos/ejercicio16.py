#Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar
#cuál fue el mayor número ingresado.


def buscaMayor():
    n = 1
    mayor = -99999999999999999999999999999999999999999999999999999999999999999999
    while n != 0:
        try:
            n = int(input("Introduce un número (0 para finalizar): "))
            if n>0:
                if n > mayor:
                    mayor = n
        except ValueError:
            print("Valor no válido.")
    print(f"El mayor número ingresado es: {mayor}")



if __name__ == "__main__":
    try:
        buscaMayor()
    except Exception as e:
        print(f"Error desconocido: {e}")