""""Escribir un programa que solicite el ingreso de una cantidad indeterminada de números 
mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números 
primos ingresados."""

def cuentaPrimos():
    contador = 0
    n = 1
    while n != 0:
        try:
            n = int(input("Introduzca un entero positivo (0 para terminar): "))
            if n <0:
                raise NameError ("NO SE ADMITEN NEGATIVOS")
            elif esPrimo(n):
                contador += 1

        except NameError:
            print("No se admiten negativos")
        except ValueError:
            print("Debe ingresar un número entero")
    print(f"Usted ha ingresado un total de {contador} numeros primos")

def esPrimo(n):
    if n<1:
        return False
    for i in range(2,int(n*0.5)+1):  #Con esto lo que hago es comprobar la primera mitad si hay divisores
        if n % i ==0:
            return False
    return True


if __name__ == "__main__":
    try:
        cuentaPrimos()
    except Exception as e:
        print(f"Error desconocido: {e}")