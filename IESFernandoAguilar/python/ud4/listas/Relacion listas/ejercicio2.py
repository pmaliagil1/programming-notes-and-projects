def invierte(lista):
    """Recibe una lista y devuelve la lista en orden inverso."""
    return lista[::-1]

n = int(input("¿Cuántas cadenas deseas ingresar? "))

lista_cadenas = []
for i in range(n):
    cadena = input(f"Ingrese la cadena {i + 1}: ")
    lista_cadenas.append(cadena)

lista_invertida = invierte(lista_cadenas)

print("Lista original:", lista_cadenas)
print("Lista invertida:", lista_invertida)
