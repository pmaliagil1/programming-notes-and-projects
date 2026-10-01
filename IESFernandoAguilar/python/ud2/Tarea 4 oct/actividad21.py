pisos = int(input("Introduce el número de pisos del árbol: "))
for numero in range (1, pisos + 1):
    asteriscos = 2 * numero -1
    espacios = pisos - numero
    print(" "*espacios + "*"*asteriscos)