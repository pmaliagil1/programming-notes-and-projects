def mayusculas(cadena):
    return cadena.upper()

def minusculas(cadena):
    return cadena.lower()

if __name__ == "__main__":

    cadena = input("Ingresa una cadena de texto: ")
    
    print("Cadena en mayúsculas:", mayusculas(cadena))
    print("Cadena en minúsculas:", minusculas(cadena))
