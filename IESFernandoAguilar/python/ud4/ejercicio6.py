def cantidad_mayusculas_minusculas(cadena):
    contador_mayusculas = 0
    contador_minusculas = 0
    
    for caracter in cadena:
        if caracter.isupper():  
            contador_mayusculas += 1
        elif caracter.islower(): 
            contador_minusculas += 1
    
    return contador_mayusculas, contador_minusculas

cadena = input("Ingresa una cadena: ")
mayusculas, minusculas = cantidad_mayusculas_minusculas(cadena)
print(f"Mayúsculas: {mayusculas}")
print(f"Minúsculas:{minusculas}")
