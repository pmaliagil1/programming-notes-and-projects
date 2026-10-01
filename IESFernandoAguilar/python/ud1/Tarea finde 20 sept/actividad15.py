parcial1 = float(input("Ingresa la calificación del primer parcial: "))
parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial3 = float(input("Ingresa la calificación del tercer parcial: "))
examen = float(input("Ingresa la calificación del examen final: "))
trabajo = float(input("Ingresa la calificación del tranajo: "))
media_parciales = (parcial1 + parcial2 + parcial3) / 3
calificación_final = (media_parciales * 0.55) + (examen * 0.3) + (trabajo * 0.15)
redondeo = round (calificación_final,2)
print ("Tu calificación final es: ",redondeo)
