import random

def shuffled_square(n):
    numbers = list(range(1, n*n + 1))
    random.shuffle(numbers)
    square = [numbers[i*n:(i+1)*n] for i in range(n)]
    return square

def is_magic_square(square):

    n = len(square)
    target_sum = sum(square[0])

    for row in square:
        if sum(row) != target_sum:
            return False

    for col in range(n):
        if sum(square[row][col] for row in range(n)) != target_sum:
            return False

    if sum(square[i][i] for i in range(n)) != target_sum:
        return False

    if sum(square[i][n-1-i] for i in range(n)) != target_sum:
        return False

    return True

if __name__ == "__main__":
    n = int(input("Introduce el tamaño del cuadrado mágico (n): "))
    square = shuffled_square(n)
    print("Matriz generada:")
    for row in square:
        print(row)

    if is_magic_square(square):
        print("Es un cuadrado mágico.")
    else:
        print("No es un cuadrado mágico.")
