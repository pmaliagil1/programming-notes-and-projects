def sustituye(cadena, caracter_a, caracter_b):

    return cadena.replace(caracter_a, caracter_b)

cadena = input("Introduce una cadena: ")
caracter_a = input("Introduce el carácter a reemplazar: ")
caracter_b = input("Introduce el nuevo carácter: ")

nueva_cadena = sustituye(cadena, caracter_a, caracter_b)
print(f"La nueva cadena es: {nueva_cadena}")
