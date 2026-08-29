 def crear_tabla():
    tabla = [[" " for _ in range(3)] for _ in range(3)]
    return tabla

def imprimir_tabla(tabla):
    x = 1
    print(" ")
    for f in tabla:
        print("|".join(f))
        if x <=2:
            print("--------")
        x += 1
    print(" ")

def hay_ganador(tablero):
    ganaror_jugador1 = False
    ganaror_jugador2 = False
    pass

def jugar():
    contador = 1

    tabla = imprimir_tabla()









if __name__=="__main__":
    jugar()