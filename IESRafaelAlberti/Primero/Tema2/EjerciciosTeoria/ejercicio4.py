"""Escribir un programa que pida al usuario un número entero y muestre por pantalla si es
par o impar. """

numero = int(input("Introduzca un número para ver si es par o impar: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Impar")