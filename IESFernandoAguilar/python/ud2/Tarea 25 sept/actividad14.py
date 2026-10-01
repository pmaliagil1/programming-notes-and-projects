dia,mes,año = input("Ingresa una fehca: ").split()
año = int(año)
mes = int(mes)
dia = int(dia)

print(f"Usted ha seleccionado el año {año}, el mes: {mes}, y el dia: {dia}")
if año >0 and mes >0 and mes <13 and dia > 0:
    if mes == 1 and dia < 31: 
        print(f"La fecha seleccionada es {dia, "enero", año}")
    elif mes == 1 and dia > 31:
        print("Fecha no válida.")
    elif mes == 2 and dia < 29: 
        print(f"La fecha seleccionada es {dia, "febrero", año}")
    elif mes == 2 and dia > 29:
        print("Fecha no válida.")
    elif mes == 3: 
        print(f"La fecha seleccionada es {dia, "marzo", año}")
    elif mes == 3 and dia > 31:
        print("Fecha no válida.")
    elif mes == 4: 
        print(f"La fecha seleccionada es {dia, "abril", año}")
    elif mes == 4 and dia > 30:
        print("Fecha no válida.")
    elif mes == 5: 
        print(f"La fecha seleccionada es {dia, "mayo", año}")
    elif mes == 5 and dia > 31:
        print("Fecha no válida.")
    elif mes == 6: 
        print(f"La fecha seleccionada es {dia, "junio", año}")
    elif mes == 6 and dia > 30:
        print("Fecha no válida.")
    elif mes == 7: 
        print(f"La fecha seleccionada es {dia, "julio", año}")
    elif mes == 7 and dia > 31:
        print("Fecha no válida.")
    elif mes == 8: 
        print(f"La fecha seleccionada es {dia, "agosto", año}")
    elif mes == 8 and dia > 31:
        print("Fecha no válida.")
    elif mes == 9: 
        print(f"La fecha seleccionada es {dia, "septiembre", año}")
    elif mes == 9 and dia > 30:
        print("Fecha no válida.")
    elif mes == 10: 
        print(f"La fecha seleccionada es {dia, "octubre", año}")
    elif mes == 10 and dia > 31:
        print("Fecha no válida.")
    elif mes == 11: 
        print(f"La fecha seleccionada es {dia, "noviembre", año}")
    elif mes == 11 and dia > 30:
        print("Fecha no válida.")
    elif mes == 12: 
        print(f"La fecha seleccionada es {dia, "diciembre", año}")
    elif mes == 12 and dia > 31:
        print("Fecha no válida.")
else: 
    print("Fecha no válida.")


