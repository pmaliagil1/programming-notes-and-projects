"""Tic-Tac-Toe, by Al Sweigart
The classic board game.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, board game, game, two-player"""

ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '  # Constantes para los valores.

def main():
    print('Welcome to Tic-Tac-Toe!')
    gameBoard = getBlankBoard()  # Crear un tablero vacío.
    currentPlayer, nextPlayer = X, O  # X comienza, O va después.

    while True:  # Bucle principal del juego.
        # Mostrar el tablero actual:
        print(getBoardStr(gameBoard))

        # Pedir al jugador su movimiento:
        move = None
        while not isValidSpace(gameBoard, move):
            print(f'What is {currentPlayer}\'s move? (1-9)')
            move = input('> ')
        updateBoard(gameBoard, move, currentPlayer)  # Realizar el movimiento.

        # Comprobar si el juego ha terminado:
        if isWinner(gameBoard, currentPlayer):  # Verificar si hay ganador.
            print(getBoardStr(gameBoard))
            print(f'{currentPlayer} has won the game!')
            break
        elif isBoardFull(gameBoard):  # Verificar si hay empate.
            print(getBoardStr(gameBoard))
            print('The game is a tie!')
            break

        # Cambiar turnos entre los jugadores:
        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    print('Thanks for playing!')

def getBlankBoard():
    """Crea un tablero vacío de tic-tac-toe."""
    board = {}
    for space in ALL_SPACES:
        board[space] = BLANK  # Todas las posiciones empiezan vacías.
    return board

def getBoardStr(board):
    """Devuelve una representación en texto del tablero."""
    return f'''
      {board['1']}|{board['2']}|{board['3']}  1 2 3
      -+-+-
      {board['4']}|{board['5']}|{board['6']}  4 5 6
      -+-+-
      {board['7']}|{board['8']}|{board['9']}  7 8 9'''

def isValidSpace(board, space):
    """Devuelve True si el espacio es válido (1-9) y está vacío."""
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    """Devuelve True si el jugador ha ganado."""
    b, p = board, player
    # Verificar filas, columnas y diagonales para tres en raya:
    return ((b['1'] == b['2'] == b['3'] == p) or  # Fila superior
            (b['4'] == b['5'] == b['6'] == p) or  # Fila media
            (b['7'] == b['8'] == b['9'] == p) or  # Fila inferior
            (b['1'] == b['4'] == b['7'] == p) or  # Columna izquierda
            (b['2'] == b['5'] == b['8'] == p) or  # Columna central
            (b['3'] == b['6'] == b['9'] == p) or  # Columna derecha
            (b['1'] == b['5'] == b['9'] == p) or  # Diagonal principal
            (b['3'] == b['5'] == b['7'] == p))    # Diagonal secundaria

def isBoardFull(board):
    """Devuelve True si todas las posiciones del tablero están ocupadas."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # Si hay un espacio vacío, no está lleno.
    return True  # Si no hay espacios vacíos, está lleno.

def updateBoard(board, space, mark):
    """Actualiza el tablero en la posición dada con la marca del jugador."""
    board[space] = mark

if __name__ == '__main__':
    main()  # Ejecutar la función principal si se ejecuta directamente.
