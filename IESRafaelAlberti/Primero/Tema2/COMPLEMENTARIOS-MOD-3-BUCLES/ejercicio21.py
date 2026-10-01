"""Escribe un programa que permita ir introduciendo una serie indeterminada de números
mientras su suma no supere el valor 10000. Cuando esto último ocurra, se debe mostrar el
total acumulado, el contador de los números introducidos y la media."""

def introduceNumeros():
    n = 0
    contador = 0
    total = 0
    while total < 10000:
        try:
            n = int(input("Introduce un número para la suma (termina al llegar al superar 10000): "))
            contador+=1
            total = total + n
        except ValueError:
            print("Valor no válido")
    media = total//contador
    return f"Total: {total}\nContador: {contador}\nMedia:{media}"


if __name__ == "__main__":
    try:
        print(introduceNumeros())
    except Exception as e:
        print(f"Algo ha salido mal: {e}")