#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar
#la sumatoria de todos los números positivos ingresados.

def sumaPositivos():
    n = 1
    suma = n
    while n != 0:
        try:
            n = int(input("Introduce un número (0 para finalizar): "))
            if n>0:
                suma+=n
        except ValueError:
            print("Valor no válido.")
    print(f"La suma de todos los positivos es de: {suma-1}")



if __name__ == "__main__":
    try:
        sumaPositivos()
    except Exception as e:
        print(f"Error desconocido: {e}")