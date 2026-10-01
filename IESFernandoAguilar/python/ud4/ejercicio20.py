def es_pangrama(cadena):
    cadena_lower = cadena.lower()
    
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    
    for letra in alfabeto:
        if letra not in cadena_lower:
            return False
            
    return True

if __name__ == "__main__":
    cadena = input("Ingresa una cadena de texto: ")

    resultado = es_pangrama(cadena)
    
    print("¿Es un pangrama?", resultado)
