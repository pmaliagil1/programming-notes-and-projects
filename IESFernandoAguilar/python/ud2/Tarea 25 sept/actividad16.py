cantidad_alumnos = int(input("Ingrese la cantidad de alumnos que van a la excursión: "))
costo_por_alumno = 0
pago_total = 0
if cantidad_alumnos >= 100:
    costo_por_alumno = 65
    pago_total = cantidad_alumnos * costo_por_alumno
    print(f"Cada alumno debe pagar: {costo_por_alumno} euros")
elif cantidad_alumnos > 49 and cantidad_alumnos < 100:
    costo_por_alumno = 70
    pago_total = cantidad_alumnos * costo_por_alumno
    print(f"Cada alumno debe pagar: {costo_por_alumno} euros")
elif cantidad_alumnos > 38 and cantidad_alumnos < 50:
    costo_por_alumno = 95
    pago_total = cantidad_alumnos * costo_por_alumno
    print(f"Cada alumno debe pagar: {costo_por_alumno} euros")
else:
    pago_total = 4000
    if cantidad_alumnos > 0:
        cantidad_alumnos / pago_total
    else:
        costo_por_alumno = 0
print (f"El pago total es de: {pago_total} euros.")
if cantidad_alumnos == 0:
 print("No hay alumnos para el viaje.")