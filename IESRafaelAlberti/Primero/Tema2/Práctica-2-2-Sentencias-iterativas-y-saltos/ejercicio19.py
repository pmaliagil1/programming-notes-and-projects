"""Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-
finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó
3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a
mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las
opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión
del menú y el programa finalizará."""


def menu():
    opcion = 0
    while opcion != 3:
        try:
            print("MENU\n1.Comenzar programa\n2.Imprimir listado\n3.Finalizar programa")
            opcion = int(input("Introduzca su opción: "))
            if opcion <1 or opcion>3:
                raise ValueError ("VALOR FUERA DE RANGO")
            elif opcion == 1:
                print("Comenzando programa")
            elif opcion == 2:
                print("Imprimiendo listado")
            elif opcion == 3:
                print("Saliendo del programa")
            else:
                raise NameError ("VALOR NO VÁLIDO")
        except ValueError:
            print("Valor no válido")


if __name__ == "__main__":
    try:
        menu()
    except NameError:
        print("Valor no válido")
    except Exception as e:
        print(f"Error desconocido: {e}")
