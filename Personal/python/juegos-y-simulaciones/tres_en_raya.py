from random import randint

def generar_tablero_inicial():
    return [[" " for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def hay_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    
    return None
def tablero_lleno(tablero):
    """Verifica si el tablero está lleno."""
    return all(celda != " " for fila in tablero for celda in fila)

def jugar():
    """Función principal que gestiona el flujo del juego."""
    print("¡Bienvenido al Tres en Raya!")
    tablero = generar_tablero_inicial()
    jugadores = ["X", "O"]
    turno_actual = randint(0, 1)
    
    while True:
        imprimir_tablero(tablero)
        print(f"Turno del jugador {jugadores[turno_actual]}")
        
        while True:
            try:
                fila = int(input("Ingresa la fila (0, 1, 2): "))
                columna = int(input("Ingresa la columna (0, 1, 2): "))
                if 0 <= fila < 3 and 0 <= columna < 3 and tablero[fila][columna] == " ":
                    break
                else:
                    print("Esa posición no está disponible, intenta de nuevo.")
            except ValueError:
                print("Entrada inválida, por favor ingresa números entre 0 y 2.")
        
        tablero[fila][columna] = jugadores[turno_actual]
        
        ganador = hay_ganador(tablero)
        if ganador:
            imprimir_tablero(tablero)
            print(f"¡Felicidades! El jugador {ganador} ha ganado.")
            break
        
        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break
        
        turno_actual = 1 - turno_actual

if __name__ == "__main__":

    jugar()
