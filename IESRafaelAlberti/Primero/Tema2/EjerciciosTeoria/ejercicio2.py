"""Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
introducida por el usuario coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas. """

contraseña = "contraseña"

respuesta = input("Introduzca su contraseña: ").lower()

if respuesta == contraseña:
    print("Su contraseña coincide con la ya guardada")

else:
    print("Contraseña guardada correctamente.")
