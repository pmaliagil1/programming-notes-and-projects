"""Escribir un programa que pregunte por una muestra de números, separados por comas, 
los guarde en una lista y muestre por pantalla su media y desviación típica."""


def calculaMedia(m): #En este programa solo tienes que hacer la formula de la desviacion tipica buscandola en google
    suma = sum(m)
    cantidad = len(m)

    resultado = suma/cantidad
    return resultado


def calculaDesviacionTipica(m):
    media = calculaMedia(m)
    sumCuadrados = 0
    cantidad = len(m)

    for numero in m:
        diferencia=numero-media
        sumCuadrados += diferencia**2

    desviacionTipica = (sumCuadrados/cantidad)
    return desviacionTipica*0.5


if __name__ == "__main__":
    entrada = input("Introduce numeros separados por comas: ")
    muestra = entrada.split(",")

    #una vez obtenida la lista de caracteres, las pasamos a numeros enteros en otra lista
    secuencia = []
    for valor in muestra:
        try:
            secuencia.append(int(valor))
        except ValueError:
            print("Este valor no es numerico")
            muestra.remove(valor)
    
    print(f"La media es: {calculaMedia(secuencia)}")
    print(f"La desviacion tipica es: {calculaDesviacionTipica(secuencia)}")