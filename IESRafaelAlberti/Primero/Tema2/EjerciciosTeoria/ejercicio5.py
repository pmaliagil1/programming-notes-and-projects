"""Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al
usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que
tributar o no"""

edad = int(input("Introduzca su edad: "))
ingresos = float(input("Introduzca sus ingresos mesuales: "))

if edad <= 16:
    print("Usted no debe tributar")

else:
    if ingresos >= 1000:
        print("Usted debe tributar")
    else:
        print("Usted no debe tributar")