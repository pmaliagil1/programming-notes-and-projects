from random import randint

def generar_tablero_inicial():
    """Genera un tablero vacío de 3x3."""
    tablero =  [[" " for _ in range(3)] for _ in range(3)]
    return tablero

def imprimir_tablero(tablero):
    """Imprime el tablero en un formato legible."""
    x = 1
    print(" ")
    for f in tablero:
        print("|".join(f))
        if x <= 2:
            print("------")
        x += 1
    print(" ")

def hay_ganador(tablero):
    ganador_jugador1 = False
    ganador_jugador2 = False
    """Verifica si hay un ganador en el tablero."""
    pass

def jugar():
    """Función principal que gestiona el flujo del juego.
    Toda la interacción con el usuario (entrada, validación, mensajes y
    lógica principal del juego) se gestiona aquí."""

    contador = 1
    turno_jugador= ""
    fila_jugador1= ""
    columna_jugador1= ""
    coordenadas_jugador1 = ""
    fila_jugador2 = ""
    columna_jugador2 = ""
    coordenadas_jugador2 = ""
    lista_posiciones_utilizadas = []

    tablero = generar_tablero_inicial()
    imprimir_tablero(tablero)

    while contador <= 9:

        if contador % 2 == 0:
            turno_jugador = "Jugador 2"

        else:
            turno_jugador = "Jugador 1"

        print(f"Es el turno de {turno_jugador}")

        if contador % 2 != 0:

            while coordenadas_jugador1 not in lista_posiciones_utilizadas:
                fila_jugador1,columna_jugador1 = map(int,input(f"Es tu turno, indica las coordenadas de la casilla (a,b):").split(","))
                fila_jugador1 =  fila_jugador1 - 1
                columna_jugador1 = columna_jugador1 - 1
                coordenadas_jugador1 = [fila_jugador1,columna_jugador1]

                if coordenadas_jugador1 not in lista_posiciones_utilizadas:
                    lista_posiciones_utilizadas.append(coordenadas_jugador1)
                    tablero[fila_jugador1][columna_jugador1] = "X"
                
                else:
                    print("Las coordenadas indicadas ya están escogidas, elige otro...")

                    while coordenadas_jugador1 in lista_posiciones_utilizadas:
                            fila_jugador1,columna_jugador1 = map(int,input(f"--> (a,b): ").split(","))
                            coordenadas_jugador1 =[fila_jugador1,columna_jugador1]

        else:

             while coordenadas_jugador2 not in lista_posiciones_utilizadas:
                fila_jugador2 = randint(0,2)
                columna_jugador2 = randint(0,2)
                coordenadas_jugador2 = [fila_jugador2,columna_jugador2]

                if coordenadas_jugador2 not in lista_posiciones_utilizadas:
                    lista_posiciones_utilizadas.append(coordenadas_jugador2)
                    tablero[fila_jugador2][columna_jugador2] = "0"
                
                else:
                    while coordenadas_jugador2 in lista_posiciones_utilizadas:
                        fila_jugador2 = randint(0,2)
                        columna_jugador2 = randint(0,2)
                        coordenadas_jugador2 = [fila_jugador2,columna_jugador2]
                
        contador += 1
        coordenadas_jugador1 = ""
        coordenadas_jugador2 = ""
        fila_jugador1 = ""
        fila_jugador2 = ""
        columna_jugador1 = ""
        columna_jugador2 = ""
        imprimir_tablero(tablero)
    ganador = hay_ganador(tablero)
    return tablero

if __name__ == "__main__":
    #No agreges ningún código aquí
    jugar()