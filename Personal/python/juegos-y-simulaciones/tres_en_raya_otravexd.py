from random import randint

def generar_tablero_inicial():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def hay_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != " ":
            return True
        
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
        return True
    return False

def jugar():
    turno_jugador = ""
    fila_jugador_1 = ""
    fila_jugador_2 = ""
    columna_jugador_1 = ""
    columna_jugador_2 = ""
    coordenadas_jugador_1 = ""
    coordenadas_jugador_2 = ""
    contador = 1
    lista_posiciones_usadas = []
    tablero = generar_tablero_inicial()
    imprimir_tablero(tablero)

    while contador <= 9:
        if contador % 2 == 0:
            turno_jugador = "Jugador 2"
        else:
            turno_jugador = "Jugador 1"
        print(f"Turno de {turno_jugador}")

        if contador % 2 != 0:
            while True:
                fila_jugador_1, columna_jugador_1 = map(int, input("Introduce las coordenadas (a,b): ").split(","))
                fila_jugador_1 -= 1  # Resta 1 para ajustar al índice de la lista
                columna_jugador_1 -= 1
                coordenadas_jugador_1 = [fila_jugador_1, columna_jugador_1]
                
                if coordenadas_jugador_1 not in lista_posiciones_usadas:
                    lista_posiciones_usadas.append(coordenadas_jugador_1)
                    tablero[fila_jugador_1][columna_jugador_1] = "X"
                    break
                else:
                    print("Coordenadas ya usadas, inténtelo de nuevo.")

        else:
            while True:
                fila_jugador_2 = randint(0, 2)
                columna_jugador_2 = randint(0, 2)
                coordenadas_jugador_2 = [fila_jugador_2, columna_jugador_2]

                if coordenadas_jugador_2 not in lista_posiciones_usadas:
                    lista_posiciones_usadas.append(coordenadas_jugador_2)
                    tablero[fila_jugador_2][columna_jugador_2] = "0"
                    break
                else:
                    print("Coordenadas ya usadas, inténtelo de nuevo.")

        imprimir_tablero(tablero)

        if hay_ganador(tablero):
            print(f"{turno_jugador} ha ganado")  
            break
        contador += 1
    if contador > 9:
        print("La partida ha quedado en empate")

if __name__ == "__main__":
    jugar()
