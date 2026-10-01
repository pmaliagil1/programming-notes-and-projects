def dia_mes_anio(fecha):
    partes = fecha.split("/")
    
    if len(partes) == 3:
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
        return dia, mes, anio
    else:
        return None

if __name__ == "__main__":
    fecha = input("Ingresa la fecha en formato dd/mm/aaaa: ")
    resultado = dia_mes_anio(fecha)

    if resultado:
        dia, mes, anio = resultado
        print(f"Día: {dia}")
        print(f"Mes: {mes}")
        print(f"Año: {anio}")
    else:
        print("Error: Ingresa la fecha en el formato correcto (dd/mm/aaaa).")
