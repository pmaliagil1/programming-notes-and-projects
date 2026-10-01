"""
Módulo: calculadora.py
Descripción: 
    Solo tiene las cuatro operaciones básicas: suma, resta, multiplicación y división.

"""

# --- FUNCIONES BÁSICAS ---

def sumar(a, b):
    """
    Suma dos números (la operación más fácil).
    
    Parámetros:
    a (int/float): El primer número.
    b (int/float): El segundo número.
    
    Retorna:
    (int/float): El resultado de la suma.
    """
    return a + b

def restar(a, b):
    """
    Resta el segundo número al primero (a - b).
    
    Parámetros:
    a (int/float): El número grande.
    b (int/float): El número que le quitamos.
    
    Retorna:
    (int/float): La diferencia.
    """
    return a - b

def multiplicar(a, b):
    """
    Multiplica dos números.
    
    Parámetros:
    a (int/float): Un número.
    b (int/float): El otro número.
    
    Retorna:
    (int/float): El resultado de la multiplicación.
    """
    return a * b

def dividir(a, b):
    """
    Divide el dividendo 'a' entre el divisor 'b' (a / b).
    
    Parámetros:
    a (int/float): El número a dividir (dividendo).
    b (int/float): El número que divide (divisor).
    
    Retorna:
    (float | str): El resultado de la división, o un mensaje si intentas dividir por cero.
    """
    # Importante revisar si el divisor es cero, si lo es, no podemos seguir.
    if b == 0:
        return "Error: ¡No se puede dividir por cero!"
    return a / b


if __name__ == "__main__":
    # Menú simple para probar las cuatro funciones.
    
    print("1.SUMAR")
    print("2.RESTAR")
    print("3.MULTIPLICAR")
    print("4.DIVIDIR")
    
    operacion = int(input("Introduce la operación que desea realizar: "))

    match operacion:
        case(1):
            a = float(input("Introduzca el primer número: "))
            b = float(input("Introduzca el segundo número: "))
            print(f"Resultado: {sumar(a,b)}")
        case(2):
            a = float(input("Introduzca el primer número: "))
            b = float(input("Introduzca el segundo número: "))
            print(f"Resultado: {restar(a,b)}")
        case(3):
            a = float(input("Introduzca el primer número: "))
            b = float(input("Introduzca el segundo número: "))
            print(f"Resultado: {multiplicar(a,b)}")
        case(4):
            a = float(input("Introduzca el dividendo: "))
            b = float(input("Introduzca el divisor: "))
            print(f"Resultado: {dividir(a,b)}")
        case _:
            print("Opción no válida.")