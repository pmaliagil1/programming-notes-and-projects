#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo. 

def triangulo(n):
    for i in range(1, n + 1, 2):        #Es la formula 2*n + 1
        for j in range(i, 0, -2):       #MIRAR BIEN ESTO A LA HORA DE ESTUDIAR
            print(j, end=" ")
        print()

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número entero: "))
        triangulo(n)
    except ValueError:
        print("Valor no valido")
    except Exception as e:
        print(f"Error desconocido: {e}")
    