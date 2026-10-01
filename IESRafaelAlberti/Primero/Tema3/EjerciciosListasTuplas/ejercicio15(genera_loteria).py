"""Genera una combinación válida para una apuesta de la lotería primitiva"""

from random import randint

def generar_combinacion_primitiva():
    numeros = []
    while len(numeros) <6:
        n = randint(1,49)
        if n not in numeros:
            numeros.append(n)
    return numeros

if __name__ == "__main__":
    combinacion = generar_combinacion_primitiva()
    print(f"La combinacion de la Primitiva es: {combinacion}")