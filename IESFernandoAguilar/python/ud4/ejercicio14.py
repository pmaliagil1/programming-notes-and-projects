def acronimo(cadena):
    return ''.join([palabra[0].upper() for palabra in cadena.split()])

if __name__ == "__main__":
    cadena = input("Ingresa una frase para obtener su acrónimo: ")
    print("Acrónimo:", acronimo(cadena))
