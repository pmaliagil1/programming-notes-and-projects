num1 = float(input("Ingrese un número para realizar la operación: "))
num2 = float(input("Ingrese un segundo número para realizar la operación: "))
operacion = input("Ingresa la operación que desea realizar (suma,resta,multiplicación o división): ")
if operacion == "suma":
    print(f"La suma de los números seleccionados es:  {num1 + num2}")
elif operacion == "resta":
    print(f"La resta de los números seleccionados es: {num1 - num2}")
elif operacion == "multiplicación":
    print(f"La multiplicación de los números seleccionados es: {num1 * num2}")
elif operacion == "división":
    if num2 == 0:
        print ("No se puede dividir entre 0")
    else:
        print(f"La división de los números seleccionados es: {num1 / num2}")
else:
    print("Operación no válida")



