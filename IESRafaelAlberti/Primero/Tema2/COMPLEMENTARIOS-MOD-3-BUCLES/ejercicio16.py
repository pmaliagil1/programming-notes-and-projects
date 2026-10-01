"""Muestra los números del 320 al 160, contando de 20 en 20 hacia atrás utilizando los tres
bucles, al igual que el ejercicio anterior."""

#VERSION BUCLE FOR
def muestraMultiplosFor():
    for i in range(320,159,-20):
        print(i)

#VERSION BUCLE WHILE
def muestraMultiplosWhile():
    i = 320
    while i > 159:
        print(i)
        i = i-20
        

#VERSION DO WHILE
def muestraMultiplosDoWhile():
    parada = False
    i = 320
    while parada == False:
        print(i)
        i = i-20
        if i < 160:
            parada = True

if __name__ == "__main__":
    try:
        muestraMultiplosFor()
        muestraMultiplosWhile()
        muestraMultiplosDoWhile()

    except Exception as e:
        print(f"Algo ha salido mal: {e}")