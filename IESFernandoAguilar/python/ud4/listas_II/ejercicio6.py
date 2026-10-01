def obtener_posicion_equipo(tabla_resultados, equipo):

    tabla_calculada = []
    for fila in tabla_resultados:
        nombre = fila[0]
        ganados = fila[1]
        empatados = fila[2]
        goles_favor = fila[4]
        goles_contra = fila[5]
        
        puntos = ganados * 3 + empatados * 1
        diferencia_goles = goles_favor - goles_contra
        tabla_calculada.append([nombre, puntos, diferencia_goles])
    
    for i in range(len(tabla_calculada) - 1):
        for j in range(len(tabla_calculada) - i - 1):
            if (tabla_calculada[j][1] < tabla_calculada[j + 1][1] or 
                (tabla_calculada[j][1] == tabla_calculada[j + 1][1] and 
                 tabla_calculada[j][2] < tabla_calculada[j + 1][2])):
                tabla_calculada[j], tabla_calculada[j + 1] = tabla_calculada[j + 1], tabla_calculada[j]
    
    posicion = 1
    for datos in tabla_calculada:
        if datos[0] == equipo:
            return (f"El equipo {equipo} terminó en la posición {posicion}, "
                    f"con {datos[1]} puntos y una diferencia de goles de {datos[2]}.")
        posicion += 1

    return f"El equipo {equipo} no está en la tabla de resultados."

tabla_epl = [
    ["Liverpool", 32, 3, 3, 85, 33],
    ["Manchester City", 26, 3, 9, 102, 35],
    ["Manchester United", 18, 12, 8, 66, 36],
    ["Chelsea", 20, 6, 12, 69, 54],
    ["Leicester City", 18, 8, 12, 67, 41],
    ["Tottenham", 16, 11, 11, 61, 47],
    ["Wolves", 15, 14, 9, 51, 40],
    ["Arsenal", 14, 14, 10, 56, 48],
    ["Sheffield United", 14, 12, 12, 39, 39],
    ["Burnley", 15, 9, 14, 43, 50],
    ["Southampton", 15, 7, 16, 51, 60],
    ["Everton", 13, 10, 15, 44, 56],
    ["Newcastle United", 11, 11, 16, 38, 58],
    ["Crystal Palace", 11, 10, 17, 31, 50],
    ["Brighton", 9, 14, 15, 39, 54],
    ["West Ham", 10, 9, 19, 49, 62],
    ["Aston Villa", 9, 8, 21, 41, 67],
    ["Bournemouth", 9, 7, 22, 40, 65],
    ["Watford", 8, 10, 20, 36, 64],
    ["Norwich", 5, 6, 27, 26, 75],
]

if __name__ == "__main__":
    equipo = input("Introduce el nombre del equipo: ")
    resultado = obtener_posicion_equipo(tabla_epl, equipo)
    print(resultado)
