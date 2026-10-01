peso = float(input("Escriba su peso en kg: " ))
estatura = float(input("Escriba su estatura en metros: "))
imc = peso / estatura ** 2
redondeo = round (imc,2)
print ("Su indice de masa corporal es ",redondeo)


