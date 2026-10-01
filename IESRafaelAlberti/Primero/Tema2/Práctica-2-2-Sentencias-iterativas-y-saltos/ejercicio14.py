#Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar
#la sumatoria de todos los números ingresados.

def sumaNumeros():
    suma = 0
    salida = 1
    while salida != 0:
        try:
            #TODOS LOS NUMEROS SE PREGUNTAN AQUI
            n = int(input("Introduce un número para sumar (0 para completar la suma): "))
            suma += n
            salida = n
        except ValueError:
            print("Valor no válido")
    return suma
# A la hora de estudiar, cuando lo hagas de nuevo ten cuidado de hacer todo dentro de la funcion
# Si no te llevarás una hora intentando que al introducir una letra el programa continue.

if __name__ == "__main__":
    try:
        #NO PREGUNTES AQUI EL PRIMER NUMERO
        total = sumaNumeros()
        print(total)

    except Exception as e:
        print(f"Error desconocido: {e}")
    except ValueError:
        print("Valor no válido")
