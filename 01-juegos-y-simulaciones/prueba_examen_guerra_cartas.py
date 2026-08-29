from random import shuffle
VALORES = tuple(range(2,15))
PALOS = ('♠', '♥', '♦', '♣')
MAX_RONDAS = 20
CARTAS_SUFICIENTES = 3

def generar_barajas():
    return [(valor,palo) for valor in VALORES for palo in PALOS]
  
def repartir(baraja):
    cantidad = len(baraja)
    mitad = cantidad // 2
    mazo1 = baraja[:mitad]
    mazo2 = baraja[mitad:]
    return mazo1, mazo2

def valor_a_figura(valor):
    match valor:
        case 11: valor_str = "J"
        case 12: valor_str = "Q"
        case 13: valor_str = "K"
        case 14: valor_str = "A"
        case _: valor_str = str(valor)
    return valor_str

def mostrar_mazo(mazo):
    for carta in mazo:
        valor,palo = carta
        valor_str = valor_a_figura(valor)
        print(f"{valor_str} {palo}", end="")

def ganador(carta1, carta2):
    valor1 = carta1[0]
    valor2 = carta2[0]
    gana = 0
    if valor1  > valor2:
        gana = 1
    elif valor2 > valor1:
        gana = 2
    return gana

def dibujar_cartas(carta1,carta2):
    valor1,palo1 = carta1
    valor2,palo2 = carta2
    valor1_str = valor_a_figura(valor1)
    valor2_str = valor_a_figura(valor2)

    print(" _____     _____")
    print(f"|{valor1_str:2}   |   |{valor2_str:2}   |")
    print(f"|  {palo1}  |   |  {palo2}  |")
    print(f"|___{valor1_str:>2}|   |___{valor2_str:>2}|")

    

