#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por comas.

def numeroImpar(n):
    if n < 0:
        raise NameError ("Número negativo no valido")
    else:
        for i in range(1,n,2):
            print(i)

if __name__ == "__main__":
    try:
        n = int(input("Introduce un entero positivo: "))
        numeroImpar(n)
    

    except NameError:
        print("Número no válido.")
    except ValueError:
        print("Valor no válido")
    except Exception as e:
        print(f"Error desconocido {e}")
