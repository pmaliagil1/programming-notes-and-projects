#Escribir un programa que pida al usuario un número entero, si la entrada no es correcta,
# mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

try:
    num = int(input("Introduce un número entero: "))
    print(f"todo ha salido bien, el número es: {num}")

except Exception as e:
    print(f"Algo ha salido mal: {e}")


