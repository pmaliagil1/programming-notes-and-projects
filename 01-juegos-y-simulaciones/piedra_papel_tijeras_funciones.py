from random import randint
PIEDRA = 1
PAPEL = 2
TIJERAS = 3


def eleccion_ordenador():
    eleccion = randint(1,3)
    if eleccion == PIEDRA:
        return "Piedra"
    elif eleccion == PAPEL:
        return "Papel"
    elif eleccion == TIJERAS:
        return "Tijeras"



def eleccion_jugador():
    while True:
        eleccion = input("Seleccione una opción ('x' para Piedra, 'p' para Papel, 't' para Tijeras): ").lower()

        if eleccion == "x":
            return "Piedra"
            
        elif eleccion == "p":
            return "Papel"

        elif eleccion == "t":
            return "Tijeras"
        
        else:
            print("Elección no válida, vuelva a intentar")
           

def ganador(eleccion_jugador_partida,eleccion):
    if eleccion_jugador == eleccion_ordenador:
        return "Empate"
    elif eleccion_jugador == "Piedra" and eleccion_ordenador == "Tijeras":
        return "Jugador"
    elif eleccion_jugador == "Papel" and eleccion_ordenador == "Piedra":
        return "Jugador"
    elif eleccion_jugador == "Tijeras" and eleccion_ordenador == "Papel":
        return "Jugador"
    elif eleccion_jugador == "Piedra" and eleccion_ordenador == "Papel":
        return "Ordenador"
    elif eleccion_jugador == "Papel" and eleccion_ordenador == "Tijeras":
        return "Ordenador"
    elif eleccion_jugador == "Tijeras" and eleccion_ordenador == "Piedra":
        return "Ordenador"
    

def jugar():
    print("Bienvenido a Piedra, Papel o Tijeras.")
    eleccion_jugador_partida = eleccion_jugador()
    eleccion_ordenador_partida = eleccion_ordenador()
    
    print(f"Tú has elegido: {eleccion_jugador_partida}")
    print(f"El ordenador ha elegido: {eleccion_ordenador_partida}")
    
    resultado = ganador(eleccion_jugador_partida, eleccion_ordenador_partida)
    
    if resultado == "Empate":
        print("¡Es un empate!")
    elif resultado == "Jugador":
        print("¡Felicidades, ganaste!")
    else:
        print("El ordenador ganó esta vez. ¡Mejor suerte la próxima!")


if __name__=="__main__":
    jugar()