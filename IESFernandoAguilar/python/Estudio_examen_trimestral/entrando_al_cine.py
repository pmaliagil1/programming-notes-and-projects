def puede_abrir_puerta(n, butacas):
    # Inicializamos una variable para indicar si encontramos un número impar
    found_odd = False
    count_even = 0
    
    # Recorremos la lista de butacas
    for butaca in butacas:
        if butaca % 2 == 0:
            # Si es par, contamos cuántas hay
            count_even += 1
        else:
            # Si es impar, verificamos si ya hemos encontrado un par
            if found_odd == False:
                found_odd = True
            # Si ya encontramos un número impar antes de los pares, no es válido
            if found_odd and butaca % 2 == 0:
                return "NO"
    
    # Si la condición se cumple, devolvemos "SI" y el número de personas con butacas pares
    return f"SI {count_even}"

# Leer el número de casos de prueba
num_casos = int(input())

for _ in range(num_casos):
    # Para cada caso de prueba
    n = int(input())  # Número de personas en la fila
    butacas = list(map(int, input().split()))  # Lista de butacas
    print(puede_abrir_puerta(n, butacas))
