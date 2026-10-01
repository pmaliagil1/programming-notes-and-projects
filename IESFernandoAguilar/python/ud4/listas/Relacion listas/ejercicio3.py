def media(notas):
    """Calcula y devuelve la media de una lista de notas."""
    return sum(notas) / len(notas)

def mas_alta(notas):
    """Devuelve la nota más alta de la lista."""
    return max(notas)

def mas_baja(notas):
    """Devuelve la nota más baja de la lista."""
    return min(notas)

def estadisticas(notas):
    """Devuelve la media, la nota más alta y la nota más baja de una lista de notas."""
    promedio = media(notas)
    nota_maxima = mas_alta(notas)
    nota_minima = mas_baja(notas)
    return promedio, nota_maxima, nota_minima

n = int(input("¿Cuántas notas deseas ingresar? "))

notas = []
for i in range(n):
    nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
    while nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10.")
        nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
    notas.append(nota)

promedio, nota_maxima, nota_minima = estadisticas(notas)

print("\nEstadísticas de las notas:")
print("Lista de notas:", notas)
print("Nota media:", promedio)
print("Nota más alta:", nota_maxima)
print("Nota más baja:", nota_minima)
