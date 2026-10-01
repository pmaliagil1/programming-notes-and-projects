lista_numeros = []

while True:
    numero = float(input("Introduce un número (introduce un número negativo para terminar): "))
    
    if numero < 0:
        break
    
    lista_numeros.append(numero)

print("\nLista de números introducidos:", lista_numeros)
