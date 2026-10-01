#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es
#un número primo o no.

def esPrimo(n):
    if n<1:
        return False
    for i in range(2,int(n*0.5)+1):  #Con esto lo que hago es comprobar la primera mitad si hay divisores
        if n % i ==0:
            return False
    return True

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número entero para ver si es primo: "))
        if esPrimo(n):
            print("El número introducido es primo")
        else:
            print("El número introducido no es primo")
    except ValueError:
        print("Valor no valido")
    except Exception as e:
        print(f"Error desconocido: {e}")