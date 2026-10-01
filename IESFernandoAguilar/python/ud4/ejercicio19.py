def es_palindromo(cadena):
    cadena_sin_espacios = ''.join(cadena.split()).lower()
    return cadena_sin_espacios == cadena_sin_espacios[::-1]

if __name__ == "__main__":
    cadena = input("Ingresa una cadena de caracteres: ")

    resultado = es_palindromo(cadena)
    
    print("¿Es palíndromo?", resultado)
