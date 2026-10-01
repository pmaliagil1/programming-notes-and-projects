def calcula_letra(numero):
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 
              'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 
              'C', 'K', 'E']
    
    resto = numero % 23
    return letras[resto]

def es_dni_valido(dni):
    if len(dni) != 9:
        return False
    
    numero_str = dni[:8]
    letra_dni = dni[8].upper() 
    
    if not numero_str.isdigit():
        return False
    
    numero = int(numero_str)
    
    letra_calculada = calcula_letra(numero)
    
    return letra_calculada == letra_dni

if __name__ == "__main__":
    dni = input("Introduce el DNI (8 números y 1 letra): ")

    if es_dni_valido(dni):
        print("El DNI es válido.")
    else:
        print("El DNI no es válido.")
