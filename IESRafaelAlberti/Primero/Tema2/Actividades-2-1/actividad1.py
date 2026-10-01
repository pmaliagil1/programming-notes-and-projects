#PRACTICAR ESTE PROGRAMA MAS EN CASA PARA CONSOLIDAR.

def numeros():

    contador = 0
    suma = 0
    media = 0

    n = ""

    while n != "fin":
        n = input("Introduzca un número (o 'fin' para terminar): ")
        if n == "fin":
            print("Hasta luego.")
        else:
            try:
                numero = float(n) 
                contador += 1
                suma += numero
                media = suma / contador
            
            except ValueError:
                print("Valor no válido")


    return suma, contador, media


if __name__ == "__main__":
    try:
        suma, contador, media = numeros()

        print(f"{suma}, {contador}, {media}")



    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
