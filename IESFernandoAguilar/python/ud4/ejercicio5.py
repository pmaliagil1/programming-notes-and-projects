def cantidad_digitos_letras(cadena):
    contador_digitos = 0
    contador_letras = 0
    
    for caracter in cadena:
        if caracter.isdigit():     
            contador_digitos += 1
        elif caracter.isalpha():   
            contador_letras += 1
    
    return contador_digitos, contador_letras

cadena = input("Ingresa una cadena: ")
digitos, letras = cantidad_digitos_letras(cadena)
print(f"Letras: {letras}")
print(f"Digitos: {digitos}")