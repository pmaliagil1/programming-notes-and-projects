pisos = int(input("Introduce el número de pisos del árbol: "))
for numero in range (1, pisos + 1):
    asteriscos = 2 * numero -1
    espacios = pisos - numero
    print(" "*espacios + "*"*asteriscos)
tronco = '|'
for _ in range(2): 
    print(tronco.center(2 * pisos - 1))