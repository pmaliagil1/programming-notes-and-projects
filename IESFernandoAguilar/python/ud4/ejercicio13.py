def reemplaza_caracter_cadena(cadena, caracter):
    return cadena.replace(" ", caracter)

if __name__ == "__main__":
    cadena = input("Ingresa una cadena de texto: ")
    caracter = input("Ingresa el carácter para reemplazar los espacios: ")

    if len(caracter) != 1:
        print("Error: Debes ingresar solo un carácter.")
    else:
        print("Cadena modificada:", reemplaza_caracter_cadena(cadena, caracter))
