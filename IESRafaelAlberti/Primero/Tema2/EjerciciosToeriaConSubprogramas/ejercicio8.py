""" En una determinada empresa, sus empleados son evaluados al final de cada año. Los
puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
A continuación, se muestra una tabla con los niveles correspondientes a cada
puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada
por la puntuación del nivel.

Nivel Puntuación
Inaceptable 0.0
Aceptable 0.4
Meritorio 0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de
rendimiento, así como la cantidad de dinero que recibirá el usuario.  """

def pintarMenu():
    print("Describe cómo es el empleado: ")
    print("1.Inaceptable")
    print("2.Aceptable")
    print("3.Meritorio")

if __name__ == "__main__":
    pintarMenu()
    try:
        opcion=int(input("Opcion: "))
        valor = 0

        match opcion:
            case 1:
                valor=0
            case 2:
                valor=0.4
            case 3:
                valor=0.6
            case _:
                print("OPCIÓN NO VÁLIDA")

        neto=2400*valor+2400
        print(f"El empleado recibirá: {neto}")
    except ValueError:
        print("La opción no puede ser alfanumérica")
    except TypeError:
        print("El cálculo ha fallado")
    except NameError:
        "VALOR NO DEFINIDO"