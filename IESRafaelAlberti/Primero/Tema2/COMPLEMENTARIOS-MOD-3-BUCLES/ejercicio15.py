"""Muestra los números múltiplos de 5 de 0 a 100 realizando tres versiones del ejercicio, una
con un bucle for, otra con un while y otra con un do-while."""

#VERSION BUCLE FOR
def muestraMultiplosFor():
    for i in range(0,101,5):
        print(i)

#VERSION BUCLE WHILE
def muestraMultiplosWhile():
    i = 0
    while i < 100:
        i = i+5
        print(i)

#VERSION DO WHILE
def muestraMultiplosDoWhile():
    parada = False
    i = 0
    while parada == False:
        i = i+5
        print(i)
        if i == 100:
            parada = True

if __name__ == "__main__":
    try:
        muestraMultiplosFor()
        muestraMultiplosWhile()
        muestraMultiplosDoWhile()
    except Exception as e:
        print(f"Algo ha salido mal: {e}")