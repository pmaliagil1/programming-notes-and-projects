def numeros():
    maximo = -9999999999999999999999
    minimo = 99999999999999999999999
    contador = 0
    suma = 0
    media = 0

    n = 0

    while n != "fin":
        n = input("Introduzca un número (o 'fin' para terminar): ")
        if n == "fin":
            maximo = 0
            minimo = 0
            print("Hasta luego.")
        else:
            try:
                n = input("Introduzca un número (o 'fin' para terminar): ")

                numero = float(n) 
                contador += 1
                suma += numero
                media = suma / contador
                if numero > maximo:
                    maximo = numero
                if numero < minimo:
                    minimo = numero
            
            except ValueError:
                print("Entrada no válida")


    return suma, contador, media, maximo, minimo


if __name__ == "__main__":
    try:
        suma, contador, media, maximo, minimo = numeros()

        print(f"{suma}, {contador}, {media}")
        print(f"Maximo: {maximo}")
        print(f"Minimo: {minimo}")


    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
