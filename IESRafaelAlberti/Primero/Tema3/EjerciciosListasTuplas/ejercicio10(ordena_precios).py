"""Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 
22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios."""

mayor = 0              #USAR METODO MAX Y MIN
menor = 0

lista = [50,75,46,22,80,65,8]

maximo = max(lista)
minimo = min(lista)

print(f"Maximo:{maximo}\nMinimo:{minimo}")

#Se puede hacer recorriendo la lista y actualizando dos variables de maximo y minimo pero asi es mas correcto