numero_total = int(input ("Escriba el número total de alumnos: "))
chicos = int(input ("Escriba el número de alumnos que son chicos: "))
chicas = int(input ("Escriba el número de alumnos que son chicas: "))
if chicos > numero_total or chicas > numero_total:
    print ("El número de chicos no puede superar al número total de alumnos")
elif chicos + chicas != numero_total:
    print ("La suma total de chicos y chicas no coindice con el número total de alumnos")

else:
    niños = numero_total - chicas
    niñas = numero_total - chicos
    print ("El número total de alumnos es: ",numero_total)
    print ("El número total de chicos es: ",niños)
    print ("El número total de chicas es: ",niñas)