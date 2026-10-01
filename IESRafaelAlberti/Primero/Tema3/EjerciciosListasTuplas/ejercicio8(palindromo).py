"""Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un 
palíndromo"""

def palindromo(palabra):         #MEJOR FORMA DEBAJO (usa reverse)
    respuesta = False              
    reverso = palabra[::-1]         #puedes usar reversed (no es lo mismo que reverse)
    if reverso == palabra:             #reverse es para listas, reversed para string 
        respuesta = True
    return respuesta


if __name__ == "__main__":
    try:
        palabra = input("Introduzca una palabra: ").lower()
        if palindromo(palabra):
            print("La palabra introducida es un palindromo.")
        else:
            print("La palabra introducida no es palindromo")
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""OTRA FORMA
palabra = input("Dime una palabra: ")

palabra1 = list(palabra)
palabra2 = list(palabra1)
palabra2.reverse()

if palabra1==palabra2:
    print("PALINDROMO")
else:
    print("NO ES PALINDROMO")
"""