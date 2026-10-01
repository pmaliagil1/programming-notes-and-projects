#Escribir un programa que pida al usuario un número entero y muestre por pantalla un
#triángulo rectángulo como el de más abajo, de altura el número introducido. 

def pintaArbol(n):
    for i in range(n):
        print("*"*i)

if __name__ == "__main__":
    try:
        n = int(input("Introduce un número entero: "))
        pintaArbol(n)
    except ValueError:
        print("Error, dato no válido")
    except Exception as e:
        print(f"Error desconocido: {e}")