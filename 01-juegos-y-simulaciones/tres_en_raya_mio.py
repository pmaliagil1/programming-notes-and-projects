from random import randint

def generar_tablero_inicial():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def hay_ganador(tablero):
    # Revisar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return True  # Gana por fila
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return True  # Gana por columna
    
    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return True  # Gana por diagonal principal
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return True  # Gana por diagonal secundaria

    return False  # No hay ganador

def jugar():
    turno_jugador = ""
    contador = 1
    fila_jugador_1 = ""
    columna_jugador_1 = ""
    coordenadas_jugador_1 = ""
    fila_jugador_2 = ""
    columna_jugador_2 = ""
    coordenadas_jugador_2 = ""
    lista_posiciones_utilizadas = []
    tablero = generar_tablero_inicial()
    imprimir_tablero(tablero)

    while contador <= 9:

        if contador % 2 == 0:
            turno_jugador = "Jugador 2"
        else:
            turno_jugador = "Jugador 1"
        print(f"Es el turno de {turno_jugador}")

        if contador % 2 != 0:  # Turno del Jugador 1
            while True:  # Bucle para validar coordenadas del Jugador 1
                fila_jugador_1, columna_jugador_1 = map(int, input("Indica las coordenadas que deseas atacar (a,b): ").split(","))
                fila_jugador_1 -= 1
                columna_jugador_1 -= 1
                coordenadas_jugador_1 = [fila_jugador_1, columna_jugador_1]

                if coordenadas_jugador_1 not in lista_posiciones_utilizadas:
                    lista_posiciones_utilizadas.append(coordenadas_jugador_1)
                    tablero[fila_jugador_1][columna_jugador_1] = "X"
                    break  # Sale del bucle si las coordenadas son válidas
                else:
                    print("Estas coordenadas ya han sido elegidas, escoja otra.")

        else:  # Turno del Jugador 2
            while True:  # Bucle para generar coordenadas válidas del Jugador 2
                fila_jugador_2 = randint(0, 2)
                columna_jugador_2 = randint(0, 2)
                coordenadas_jugador_2 = [fila_jugador_2, columna_jugador_2]

                if coordenadas_jugador_2 not in lista_posiciones_utilizadas:
                    lista_posiciones_utilizadas.append(coordenadas_jugador_2)
                    tablero[fila_jugador_2][columna_jugador_2] = "0"
                    break  # Sale del bucle si las coordenadas son válidas

        imprimir_tablero(tablero)

        # Revisar si hay ganador
        if hay_ganador(tablero):
            print(f"¡{turno_jugador} ha ganado!")
            break  # Termina el juego si hay un ganador

        contador += 1

    # Mensaje si el juego termina sin ganador
    if contador > 9:
        print("¡El juego ha terminado en empate!")

if __name__ == "__main__":
    jugar()
