"""3. Contador de Vocales: Crea una función contar_vocales(texto) que reciba una
cadena de texto y devuelva cuántas vocales (a, e, i, o, u) conAene."""

def cuentaVocales(cadena):
    VOCALES = ["a","e","i","o","u"]
    contador = 0
    for letra in cadena:
        if letra in VOCALES:
            contador+=1
    print(f"Hay un total de {contador} vocales")


if __name__ == "__main__":

    cadena = input("Introduzca una cadena de texto: ").lower()
    cuentaVocales(cadena)