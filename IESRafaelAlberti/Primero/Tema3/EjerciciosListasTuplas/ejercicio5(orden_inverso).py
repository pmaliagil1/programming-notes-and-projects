"""Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre 
por pantalla en orden inverso separados por comas."""

def ordenInverso():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    numeros.reverse()
    resultado = ""
    for n in numeros:
        resultado += str(n) + ","
    return resultado[:-1]
    



if __name__ == "__main__":
    try:
        print(ordenInverso())
    except Exception as e:
        print(f"Algo ha salido mal: {e}")
