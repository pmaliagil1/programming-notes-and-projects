import random

def inicializar_tablero(tamaño):
    """
    Crea un tablero vacío.
    """
    return [["~" for _ in range(tamaño)] for _ in range(tamaño)]

def imprimir_tablero(tablero, ocultar_barcos=True):
    """
    Muestra el tablero en pantalla.
    """
    print("  " + " ".join(str(i) for i in range(len(tablero[0]))))
    for i, fila in enumerate(tablero):
        fila_mostrar = [celda if celda != "B" or not ocultar_barcos else "~" for celda in fila]
        print(f"{i} " + " ".join(fila_mostrar))

def colocar_barcos(tablero, cantidad):
    """
    Coloca barcos aleatoriamente en el tablero.
    """
    tamaño = len(tablero)
    barcos_colocados = 0

    while barcos_colocados < cantidad:
        x = random.randint(0, tamaño - 1)
        y = random.randint(0, tamaño - 1)

        if tablero[x][y] == "~":  # Espacio disponible
            tablero[x][y] = "B"
            barcos_colocados += 1

def pedir_coordenadas():
    """
    Pide al usuario coordenadas para atacar.
    """
    while True:
        try:
            x = int(input("Introduce la fila: "))
            y = int(input("Introduce la columna: "))
            return x, y
        except ValueError:
            print("Por favor, introduce números válidos.")

def atacar(tablero, x, y):
    """
    Realiza un ataque en las coordenadas dadas.
    """
    if tablero[x][y] == "B":
        tablero[x][y] = "X"  # Barco hundido
        print("¡Tocado!")
        return True
    elif tablero[x][y] == "~":
        tablero[x][y] = "O"  # Agua
        print("¡Agua!")
    else:
        print("Ya atacaste aquí.")
    return False

def contar_barcos(tablero):
    """
    Cuenta los barcos restantes en el tablero.
    """
    return sum(fila.count("B") for fila in tablero)

def jugar_hundir_la_flota():
    """
    Función principal para jugar Hundir la Flota.
    """
    tamaño_tablero = 5
    cantidad_barcos = 3

    print("¡Bienvenido a Hundir la Flota!")
    print(f"El tablero tiene un tamaño de {tamaño_tablero}x{tamaño_tablero} y hay {cantidad_barcos} barcos por encontrar.")

    tablero = inicializar_tablero(tamaño_tablero)
    colocar_barcos(tablero, cantidad_barcos)

    barcos_restantes = cantidad_barcos
    intentos = 0

    while barcos_restantes > 0:
        imprimir_tablero(tablero)
        print(f"Barcos restantes: {barcos_restantes}")

        x, y = pedir_coordenadas()

        if 0 <= x < tamaño_tablero and 0 <= y < tamaño_tablero:
            if atacar(tablero, x, y):
                barcos_restantes -= 1
            intentos += 1
        else:
            print("Coordenadas fuera del tablero. Intenta de nuevo.")

    imprimir_tablero(tablero, ocultar_barcos=False)
    print(f"¡Felicidades! Hundiste todos los barcos en {intentos} intentos.")

if __name__ == "__main__":
    jugar_hundir_la_flota()
