"""4. Filtrado de Listas y Comprensión: Dada la lista numeros = [12, 5, 8, 19, 24, 3, 11,
40], genera una nueva lista usando list comprehension que contenga solo los
números pares mulAplicados por 2."""

def generaLista(numeros):
    nuevaLista = [numero*2 for numero in numeros if numero % 2 == 0]

    print(f"Lista antigua: {numeros}\nLista nueva: {nuevaLista}")

if __name__ == "__main__":
    numeros = [12, 5, 8, 19, 24, 3, 11, 40]
    generaLista(numeros)