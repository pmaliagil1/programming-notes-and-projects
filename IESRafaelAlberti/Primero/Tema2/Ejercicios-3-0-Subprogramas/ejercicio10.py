#Ejercicio 10: Evaluar si una edad permite votar
def edadPermitida(edad):
    if edad >= 18:
        respuesta = "Usted puede votar"
    else:
        respuesta= "Usted no puede votar"
    return (respuesta)

if __name__ == "__main__":
    edad = int(input("Introduce tu edad para ver si puede votar (+18): "))
    print(edadPermitida(edad))
