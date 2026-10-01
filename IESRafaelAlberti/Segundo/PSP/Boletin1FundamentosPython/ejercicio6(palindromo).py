"""6. Detector de Palíndromos (Strings): Escribe una función es_palindromo(cadena)
que devuelva True si la palabra o frase se lee igual de izquierda a derecha que de
derecha a izquierda (ignorando espacios y mayúsculas/minúsculas)."""

def detectaPalindromos(palabra):
    esPalindromo = False
    invertida = palabra[::-1]
    if palabra == invertida:
        esPalindromo = True
    print(esPalindromo)




if __name__ == "__main__":
    palabra = input("Introduzca una palabra: ")
    detectaPalindromos(palabra)