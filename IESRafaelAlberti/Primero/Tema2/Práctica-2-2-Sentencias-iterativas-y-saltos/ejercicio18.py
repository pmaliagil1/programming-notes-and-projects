def sumaDigitos():
    pares = 0
    n = None
    
    try:
        n_input = input("Introduce un entero positivo (-1 para terminar): ")
        n = int(n_input)
    except ValueError:
        print("Valor no válido. Terminando.")
        return

    while n != -1:
        
        if n >= 0:
            if n % 2 == 0:
                pares += 1
            
            cadena = str(n)
            suma = 0
            for digito_cadena in cadena:
                suma += int(digito_cadena)
                
            print(f"La suma de los dígitos de {n} es: {suma}")
        
        else:
            print("Número negativo no válido. Intenta con un entero positivo.")
        
        try:
            n_input = input("Introduce un entero positivo (-1 para terminar): ")
            n = int(n_input)
        except ValueError:
            print("Valor no válido. Terminando el bucle.")
            n = -1 
            
    print("Bucle terminado.")
    print(f"En total se ingresaron {pares} números pares positivos/cero (excluyendo el -1).")


if __name__ == "__main__":
    try:
        sumaDigitos()
    except Exception as e:
        print(f"Error desconocido: {e}")