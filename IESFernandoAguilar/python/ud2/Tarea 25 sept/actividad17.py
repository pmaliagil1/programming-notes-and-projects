costo_base = 0.0
impuesto = 0.0
duracion = int(input("Introduce la duración de la llamada: "))
dia = input("Introduce el día de la semana: ")
turno = input("Introduce el turno (mañana o tarde): ")

if duracion <= 5:
    costo_base = 1.0
elif duracion <= 8: 
    costo_base = 1.0 + (duracion - 5) * 0.80
elif duracion <= 10:  
    costo_base = 1.0 + 3 * 0.80 + (duracion - 8) * 0.70
else:  
    costo_base = 1.0 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50
match dia:
    case "domingo":
        impuesto = 0.03  
    case _:
        match turno:
            case "mañana":
                impuesto = 0.15  
            case "tarde":
                impuesto = 0.10  

costo_total = costo_base * (1 + impuesto)
print(f"Costo base de la llamada: {costo_base:.2f} euros")
print(f"Impuesto aplicado: {impuesto * 100:.2f}%")
print(f"Costo total a pagar: {costo_total:.2f} euros")