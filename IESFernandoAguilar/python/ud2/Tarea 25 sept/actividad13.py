anio = (int(input("Introduzca un año: ")))
if anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0:
    print ("El año introducido es bisiesto.")
elif anio % 4 == 0 and not anio % 100 == 0:
    print ("El año introducido es bisiesto.")
else:
    print ("El año introducido no es bisiesto.")


