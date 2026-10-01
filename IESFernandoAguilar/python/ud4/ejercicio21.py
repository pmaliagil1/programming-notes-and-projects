def mayusculas(cadena):
    resultado = ""
    for caracter in cadena:
        if 'a' <= caracter <= 'z':
            resultado += chr(ord(caracter) - 32)
        else:
            resultado += caracter
    return resultado

if __name__ == "__main__":
    cadena = input("Ingresa una cadena en minúsculas: ")

    cadena_mayusculas = mayusculas(cadena)

    print("Cadena en mayúsculas:", cadena_mayusculas)
