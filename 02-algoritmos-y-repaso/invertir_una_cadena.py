def invertir(cadena):
    if cadena == "":
        return ""
    return cadena[-1] + invertir(cadena[:-1])

if __name__ == "__main__":
    cadena = input()
    print(invertir(cadena))
