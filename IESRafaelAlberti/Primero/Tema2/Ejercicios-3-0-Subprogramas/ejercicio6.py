#Ejercicio 6: Convertir grados Celsius a Fahrenheit

def conversion(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

if __name__ == "__main__":
    celsius = int(input("Introduce los grados celsius para pasar a farenheit: "))
    print(conversion(celsius))