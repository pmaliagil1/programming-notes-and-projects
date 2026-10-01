#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es
#par o impar.

def parImpar(n):
    if n%2 == 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número para ver si es par o impar: "))
    except TypeError:
        print("Valor introducido incorrecto")
    except ValueError:
        print("Valor incorrecto")
    else:
        if parImpar(n):
            print("Es par")
        else:
            print("Es impar")
