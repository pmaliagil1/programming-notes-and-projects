def iniciales_mayuscula(nombre_completo):
    palabras = nombre_completo.split()
    iniciales = ''.join([palabra[0].upper() for palabra in palabras])
    return iniciales

nombre_completo = input("Introduce tu nombre completo: ")
iniciales = iniciales_mayuscula(nombre_completo)
print(f"Las iniciales en mayúscula son: {iniciales}")
