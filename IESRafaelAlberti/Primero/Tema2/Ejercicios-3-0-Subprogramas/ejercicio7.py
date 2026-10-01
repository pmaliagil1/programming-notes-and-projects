#Ejercicio 7: Contar vocales, en una palabra

def contarVocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return (contador)
if __name__ == "__main__":
    palabra = input("Introduce una palabra: ")
    print(contarVocales(palabra))