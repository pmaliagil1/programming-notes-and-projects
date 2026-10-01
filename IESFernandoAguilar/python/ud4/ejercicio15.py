def capitaliza(cadena):
    return cadena.title()

if __name__ == "__main__":
    cadena = input("Ingresa una frase para capitalizar cada palabra: ")

    print("Cadena capitalizada:", capitaliza(cadena))
