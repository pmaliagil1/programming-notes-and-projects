"""Realiza un programa que pida una hora por teclado y que muestre luego buenos días,
buenas tardes o buenas noches según la hora. Se utilizarán los tramos de 6 a 12, de 13 a 20 y de
21 a 5. respectivamente. Sólo se tienen en cuenta las horas, los minutos no se deben introducir por
teclado."""

def saludoHora(hora):
    if hora >=6 and hora <=12:
        return "Buenos dias"
    elif hora >=13 and hora <=20:
        return "Buenas tardes"
    elif hora >= 21 and hora <= 24 or hora >= 1 and hora <= 5:
        return "Buenas noches"
    else:
        raise ValueError("DATO NO VALIDO")

if __name__ == "__main__":
    try:
        hora = int(input("Introduce la hora: "))
        print(saludoHora(hora))
    except ValueError:
        print("Dato no válido")
    except Exception as e:
        print(f"Algo ha salido mal {e}")
    
