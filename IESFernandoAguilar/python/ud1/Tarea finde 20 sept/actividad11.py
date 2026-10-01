celsius = float ( input("Ingrese una temperatura en grados Celsius "))
farenheit = float (input("Ingrese una temperatura en grados Farenheit "))
cel = (celsius * 1.8) + 32 
far = (farenheit -32)/1.8
redondeo = round (far,2)
red = round (cel,2)
print ("Su temperatura de Celsius a Farenheit es de ",red)
print ("Su temperatura de Farenheit a Celsius es de ",redondeo)