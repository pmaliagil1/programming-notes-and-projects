"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número 
de veces que contiene cada vocal"""

def cuentaVocales(palabra):    #MEJOR FORMA DEBAJO
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    vocales = ["a","e","i","o","u"]
    contador = 0
    for x in range(len(palabra)):
        if palabra[contador] in vocales:
            if palabra[contador] == "a":
                a+=1
            elif palabra[contador] == "e":
                e+=1
            elif palabra[contador] == "i":
                i+=1
            elif palabra[contador]== "o":
                o+=1
            elif palabra[contador]=="u":
                u+=1
        contador+=1
    return f"A:{a}\nE:{e}\nI:{i}\nO:{o}\nU:{u}"


if __name__ == "__main__":
    try:
        palabra = input("Introduce una palabra: ")
        print(cuentaVocales(palabra))
    except Exception as e:
        print(f"Algo ha salido mal: {e}")

"""
OTRA FORMA (MUCHO MEJOR):

palabra = input("Dime una palabra: ")

palabra = list(palabra)
for vocal in 'aeiou':
    if vocal in palabra:
        print(f'La vocal {vocal} esta {palabra.count(vocal) veces repetida})
"""