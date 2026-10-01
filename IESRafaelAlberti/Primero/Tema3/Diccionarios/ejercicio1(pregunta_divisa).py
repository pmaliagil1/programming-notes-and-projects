"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo
o un mensaje de aviso si la divisa no está en el diccionario."""

d = {'Euro':'€','Dollar':'$', 'Yen':'¥'}

divisa = input("Introduce la divisa que quieras: ").capitalize()
if divisa in d:
    print(d[divisa])
else:
    print("La divisa no esta en el diccionario")