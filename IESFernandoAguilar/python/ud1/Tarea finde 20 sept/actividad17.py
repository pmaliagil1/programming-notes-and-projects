minutos = float(input("Inserte el número de minutos: "))
horas = minutos // 60
min = minutos % 60
redondeo = round (horas)
red = round (min)
print ("El resultado en horas y minutos: ",redondeo, " horas y ",red," minutos.")