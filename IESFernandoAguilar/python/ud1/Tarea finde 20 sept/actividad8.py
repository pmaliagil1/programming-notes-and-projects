precio_normal = 3.49
pan_no_fresco = int(input("Escriba el número de barras de pan vendidas que no son del día: "))
precio_descuento = precio_normal * 0.6
coste_final = pan_no_fresco * precio_normal * 0.4
print ("El precio habitual del pan es de 3.49€")
print ("El descuento aplicado por no ser barras del dia es del 60%")
print ("El descuento aplicado a cada barra es de", precio_descuento)
redondeo = round (coste_final,2)
print ("El precio total es de ", redondeo)
