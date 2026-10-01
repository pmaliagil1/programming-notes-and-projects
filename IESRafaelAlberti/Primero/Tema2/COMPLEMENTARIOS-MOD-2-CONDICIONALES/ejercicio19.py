"""Escribe un programa que pida por teclado un día de la semana y que diga qué asignatura toca a
primera hora ese día."""

def primeraAsignatura(dia):
    if dia.lower() == "lunes":
        return f"La primera asignatura del {dia} es programación "
    elif dia.lower() == "martes":
        return f"La primera asignatura del {dia} es IPE "
    elif dia.lower() == "miercoles":
        return f"La primera asignatura del {dia} es base de datos "
    elif dia.lower() == "jueves":
        return f"La primera asignatura del {dia} es ENDES "
    elif dia.lower() == "viernes":
        return f"La primera asignatura del {dia} es lenguaje de marcas "
    elif dia.lower() == "sabado" or dia.lower() == "domingo":
        raise NameError ("NO HAY CLASES")
    else:
        raise TypeError("No válido")


if __name__ == "__main__":
    try:
        dia = input("Introduce un día de la semana: ")
        print(primeraAsignatura(dia))
    except NameError:
        print("Este día no hay clases")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")