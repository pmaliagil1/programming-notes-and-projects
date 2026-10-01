import random

# Constantes:
NUM_CAMBIOS = 16  # Número de intercambios entre cartas

# Caracteres de los palos de las cartas:
CORAZONES = chr(9829)  # Carácter 9829 es '♥'
DIAMANTES = chr(9830)  # Carácter 9830 es '♦'
ESPADAS = chr(9824)  # Carácter 9824 es '♠'
TREBOLES = chr(9827)  # Carácter 9827 es '♣'

# Índices de una lista de 3 cartas:
IZQUIERDA = 0
CENTRO = 1
DERECHA = 2

def dibujar_cartas(carta1, carta2, carta3):
    """Dibuja las tres cartas lado a lado."""
    filas = ["", "", "", ""]
    cartas = [carta1, carta2, carta3]
    for carta in cartas:
        valor, palo = carta
        # Ajustar alineación manualmente si el valor tiene un solo carácter.
        if len(valor) == 1:
            valor_izq = valor + " "
            valor_der = " " + valor
        else:
            valor_izq = valor
            valor_der = valor

        filas[0] += f" _____   "
        filas[1] += f"|{valor_izq}   |  "
        filas[2] += f"|  {palo}  |  "
        filas[3] += f"|___{valor_der}|  "

    for fila in filas:
        print(fila)

def obtenerCartaAleatoria():
    """Devuelve una carta aleatoria que NO sea la Reina de Corazones."""
    while True:  # Genera cartas hasta que no sea la Reina de Corazones.
        valor = random.choice(list('23456789JQKA') + ['10'])
        palo = random.choice([CORAZONES, DIAMANTES, ESPADAS, TREBOLES])

        # Devuelve la carta siempre que no sea la Reina de Corazones:
        if valor != 'Q' or palo != CORAZONES:
            return (valor, palo)

def main():
    print('Monte de Tres Cartas')
    print('Encuentra a la dama roja (la Reina de Corazones). ¡Sigue el movimiento de las cartas!')
    print()

    # Muestra la disposición inicial:
    cartas = [('Q', CORAZONES), obtenerCartaAleatoria(), obtenerCartaAleatoria()]
    random.shuffle(cartas)  # Coloca la Reina de Corazones en una posición aleatoria.
    print('Estas son las cartas:')
    dibujar_cartas(cartas[0], cartas[1], cartas[2])
    input('Presiona Enter cuando estés listo para comenzar...')

    # Realiza los intercambios:
    for i in range(NUM_CAMBIOS):
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

    # Imprime varias líneas para ocultar los intercambios.
    print('\n' * 60)

    # Pregunta al usuario dónde está la Reina de Corazones:
    while True:
        print('¿Cuál carta tiene la Reina de Corazones? (IZQUIERDA CENTRO DERECHA)')
        eleccion = input('> ').upper()

        # Obtiene el índice correspondiente a la posición elegida:
        if eleccion in ['IZQUIERDA', 'CENTRO', 'DERECHA']:
            if eleccion == 'IZQUIERDA':
                indiceEleccion = 0
            elif eleccion == 'CENTRO':
                indiceEleccion = 1
            elif eleccion == 'DERECHA':
                indiceEleccion = 2
            break

    # Muestra todas las cartas.
    dibujar_cartas(cartas[0], cartas[1], cartas[2])

    # Verifica si el jugador ganó:
    if cartas[indiceEleccion] == ('Q', CORAZONES):
        print('¡Ganaste!')
        print('¡Gracias por jugar!')
    else:
        print('¡Perdiste!')
        print('Gracias por jugar.')

if __name__ == "__main__":
    main()
