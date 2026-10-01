"""2. Clasificador de Edades: Escribe un script que solicite una edad y muestre si la
persona es menor de edad (menor a 18), adulta (18 a 64) o jubilada (65 o más)."""

def calificaEdad(edad):
    if edad <19:
        print("Menor de edad")
    elif edad>18 and edad<65:
        print("Adulta")
    elif edad >64:
        print("Jubilada")
    else:
        print("Edad introducida no válida")


if __name__ == "__main__":

    edad = int(input("Introduzca una edad: "))
    calificaEdad(edad)