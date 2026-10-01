lado1 = float(input("Introduzca el valor del primer lado de un triángulo: "))
lado2 = float(input("Introduzca el valor del segundo lado de un triángulo: "))
lado3 = float(input("Introduzca el valor del tercer lado de un triángulo (Hipotenusa): "))
if lado1**2 + lado2**2 == lado3**2:
    print("Es un triángulo rectángulo.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triángulo isósceles.")
elif lado1 == lado2 == lado3:
    print("Es un triángulo equilátero.")
else:
    print ("Es un triángulo escaleno.")

