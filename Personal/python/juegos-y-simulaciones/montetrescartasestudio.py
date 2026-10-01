from random import choice
from random import shuffle
NUMERO_CAMBIOS = 16
CORAZONES = chr(9829)  # Carácter 9829 es '♥'
DIAMANTES = chr(9830)  # Carácter 9830 es '♦'
ESPADAS = chr(9824)  # Carácter 9824 es '♠'
TREBOLES = chr(9827)  # Carácter 9827 es '♣'

IZQUIERDA = 0
CENTRO = 1
DERECHA = 0

def dibujar_cartas(carta1,carta2,carta3):
    filas = [" ", " ", " ", " "]
    cartas =[carta1, carta2, carta3]

    for carta in cartas:
        valor,palo = carta
        filas[0]+=f"___"
        filas[1]+=f"|{valor}  |"
        filas[2]+=f"| {palo} |"
        filas[3]+=f"|__{valor}|"

    for fila in filas:
        print (filas)

def obtener_carta_aleatoria():
    while True:
        palo = choice([CORAZONES,DIAMANTES,TREBOLES,ESPADAS])
        valor = choice(list(("23456789JQKA"))+["10"])

        if valor != "Q" or palo != CORAZONES:
            return(valor,palo)
        
def jugar():
    print("Bienvenido a monte tres cartas")
    print("Encuentra la reina de corazones para ganar")
    print()

    cartas = [("Q",CORAZONES), obtener_carta_aleatoria(), obtener_carta_aleatoria()]
    shuffle(cartas)
    print("Esta son las cartas")
    dibujar_cartas(cartas[0],cartas[1],cartas[2])
    input("Presiona enter para comenzar")

    for i in range (NUMERO_CAMBIOS):
        cambio = choice(["i-c","i-d","c-i","c-d","d,i","d,c"])
        if cambio == "i-c":
            print("Intercambiando izquierda y centro")
            cartas[IZQUIERDA],cartas[CENTRO] = cartas[CENTRO],cartas[IZQUIERDA]
        elif cambio == "i-d":
            print("Intercambiando izquierda y derecha")
            cartas[IZQUIERDA], cartas[DERECHA] = cartas[DERECHA],cartas[IZQUIERDA]
        elif cambio == "c-i":
            print("Intercambiando centro y izquierda")
            cartas[CENTRO],cartas[IZQUIERDA] = cartas[IZQUIERDA],cartas[CENTRO]
        elif cambio == "c-d":
            print("Intercambiando centro y derecha")
            cartas[CENTRO],cartas[DERECHA] = cartas[DERECHA],cartas[CENTRO]
        elif cambio == "d-i":
            print("Intercambiando derecha y izquierda")
            cartas[DERECHA], cartas[IZQUIERDA] = cartas[IZQUIERDA], cartas[DERECHA]
        elif cambio == "d,c":
            print("Intercambiando derecha y centro")
            cartas[DERECHA], cartas[CENTRO] = cartas[CENTRO],cartas[DERECHA]
    
    while True:
        print("Cual es la reina de corazones")
        eleccion = input().upper()

        if eleccion in ["IZQUIERDA","CENTRO","DERECHA"]:
            if eleccion == "IZQUIERDA":
                posicionEleccion = 0
            elif eleccion == "CENTRO":
                posicionEleccion = 1
            elif eleccion == "DERECHA":
                posicionEleccion = 2
            break
    dibujar_cartas(cartas[0],cartas[1],cartas[2])
