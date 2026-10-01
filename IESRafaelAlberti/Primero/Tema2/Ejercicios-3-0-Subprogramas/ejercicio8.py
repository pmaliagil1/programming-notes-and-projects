#Ejercicio 8: Mostrar línea decorativa con guiones

def lineaGuiones(numeroGuiones):
    dibujo = "-"*numeroGuiones
    return (dibujo)

if __name__ == "__main__":
    numero = int(input("Introduce el número de guiones que quieres que se pinte: "))
    print(lineaGuiones(numero))