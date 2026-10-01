num1, num2, num3 = input("Ingresa tres valores: ").split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
print(f"Usted ha seleccionado como primer valor: {num1}, como segundo valor: {num2}, y como tercer valor: {num3}")
if num1 >= num2 and num2 >= num3:
    print(f"El orden de los valores seleccionados es: {num1}, {num2}, {num3}")
elif num1 >= num3 and num3 >= num2:
    print(f"El orden de los valores seleccionados es: {num1}, {num3}, {num2}")
elif num2 >= num1 and num1 >= num3:
    print(f"El orden de los valores seleccionados es: {num2}, {num1}, {num3}")
elif num2 >= num3 and num3 >= num1:
    print(f"El orden de los valores seleccionados es: {num2}, {num3}, {num1}")
elif num3 >= num1 and num1 >= num2:
    print(f"El orden de los valores seleccionados es: {num3}, {num1}, {num2}")
elif num3 >= num2 and num2 >= num1:
    print(f"El orden de los valores seleccionados es: {num3}, {num2}, {num1}")
else:
    print("Valores no válidos.")



    


