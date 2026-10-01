#Ejercicio 9: Calcular el área de un rectángulo

def calcularArea(base, altura):
    resultado = base*altura
    return (resultado)

if __name__ == "__main__":
    base = int(input("Introduce la base: "))
    altura = int(input("Introduce la altura: "))
    print(calcularArea(base, altura))