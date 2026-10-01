import random

NUMERO_CAMBIOS = 16

CORAZONES = chr(9829)  # Carácter 9829 es '♥'
DIAMANTES = chr(9830)  # Carácter 9830 es '♦'
ESPADAS = chr(9824)  # Carácter 9824 es '♠'
TREBOLES = chr(9827)  # Carácter 9827 es '♣'

IZQUIERDA = 0
CENTRO = 1
DERECHA = 2

def dibujar_cartas(carta1, carta2, carta3):
    filas = ["", "", "", ""]
    cartas = [carta1, carta2, carta3]


    for carta in cartas:
        valor, palo = carta
        filas[0] += " ____   "
        filas[1] += f"| {valor:<2} |  "
        filas[2] += f"|  {palo} |  "
        filas[3] += f"|__{valor:>2}|  "

    for fila in filas:
        print(fila)

def obtener_carta_aleatoria():
    while True:
        valor = random.choice(list("23456789JQKA") + ["10"])
        palo = random.choice([CORAZONES, DIAMANTES, ESPADAS, TREBOLES])

        if valor != "Q" or palo != CORAZONES:
            return (valor, palo)

def jugar():
    print("Monte tres cartas")
    print("Encuentra la Reina de corazones, sigue las cartas")
    print()

    cartas = [("Q", CORAZONES), obtener_carta_aleatoria(), obtener_carta_aleatoria()]
    random.shuffle(cartas)
    print("Estas son las cartas:")
    dibujar_cartas(cartas[0], cartas[1], cartas[2])
    input("Presiona Enter para comenzar")

    for i in range(NUMERO_CAMBIOS):
        cambio = random.choice(['i-c', 'c-d', 'i-d', 'c-i', 'd-c', 'd-i'])

        if cambio == 'i-c':
            print('Intercambiando izquierda y centro...')
            cartas[IZQUIERDA], cartas[CENTRO] = cartas[CENTRO], cartas[IZQUIERDA]
        elif cambio == 'c-d':
            print('Intercambiando centro y derecha...')
            cartas[CENTRO], cartas[DERECHA] = cartas[DERECHA], cartas[CENTRO]
        elif cambio == 'i-d':
            print('Intercambiando izquierda y derecha...')
            cartas[IZQUIERDA], cartas[DERECHA] = cartas[DERECHA], cartas[IZQUIERDA]
        elif cambio == 'c-i':
            print('Intercambiando centro e izquierda...')
            cartas[CENTRO], cartas[IZQUIERDA] = cartas[IZQUIERDA], cartas[CENTRO]
        elif cambio == 'd-c':
            print('Intercambiando derecha y centro...')
            cartas[DERECHA], cartas[CENTRO] = cartas[CENTRO], cartas[DERECHA]
        elif cambio == 'd-i':
            print('Intercambiando derecha e izquierda...')
            cartas[DERECHA], cartas[IZQUIERDA] = cartas[IZQUIERDA], cartas[DERECHA]

    while True:
        print('¿Cuál carta tiene la Reina de Corazones? (IZQUIERDA CENTRO DERECHA)')
        eleccion = input('> ').upper()

        if eleccion in ['IZQUIERDA', 'CENTRO', 'DERECHA']:
            if eleccion == 'IZQUIERDA':
                posicionEleccion = 0
            elif eleccion == 'CENTRO':
                posicionEleccion = 1
            elif eleccion == 'DERECHA':
                posicionEleccion = 2
            break

    dibujar_cartas(cartas[0], cartas[1], cartas[2])

    if cartas[posicionEleccion] == ('Q', CORAZONES):
        print('¡Ganaste!')
        print('¡Gracias por jugar!')
    else:
        print('¡Perdiste!')
        print('Gracias por jugar.')

if __name__ == "__main__":
    jugar()
