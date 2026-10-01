def oculta_cadena(cadena, caracter):
    return caracter * len(cadena)

if __name__ == "__main__":
    cadena = input("Ingresa una cadena de texto: ")
    caracter = input("Ingresa el carácter para reemplazar la cadena: ")

    if len(caracter) != 1:
        print("Error: Debes ingresar solo un carácter.")
    else:
        print("Cadena oculta:", oculta_cadena(cadena, caracter))
