nota = float(input("Introduzca su nota: "))
edad = int(input("Introduzca su edad: "))
sexo = input("Introduzca su sexo: ")
if nota >= 5 and edad >= 18 and sexo == "F":
    print ("ACEPTADA")
elif nota >= 5 and edad >= 18 and sexo == "M":
    print ("POSIBLE")
else:
    print ("NO ACEPTADA")