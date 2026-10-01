"""
Módulo: calculadora.py
Descripción: 
    Este es mi proyecto de calculadora con varias funciones útiles. 
    Tenemos desde calcular la raíz cuadrada y factoriales hasta resolver 
    ecuaciones de segundo grado. Todo en un solo archivo


"""

def raizCuadrada(n):
    """
    Calcula la raíz cuadrada de un número.
    
    Parámetros:
    n (int/float): El número al que le vamos a buscar la raíz.
    
    Retorna:
    (float): La raíz cuadrada.
    """
    raiz = n ** 0.5
    # Usamos ** 0.5 que es la forma corta y fácil de sacar la raíz cuadrada.
    return raiz

def factorial(n):
    """
    Calcula el factorial de un número 'n' (se escribe n!).
    
    Recuerda que el factorial es multiplicar 'n' por todos los números anteriores hasta el 1.
    
    Parámetros:
    n (int): El número al que le queremos calcular el factorial.
    
    Retorna:
    (int): El resultado del factorial.
    """
    resultado = 1
    # Este bucle va multiplicando el resultado por cada número desde 1 hasta 'n'.
    for i in range (1,n+1):
        resultado = resultado * i
    return resultado

def potencia (a,b):
    """
    Calcula una potencia: 'a' elevado a 'b' (a^b).
    
    Parámetros:
    a (int/float): La base (el número que se multiplica).
    b (int/float): El exponente (las veces que se multiplica).
    
    Retorna:
    (int/float): El resultado de la potencia.
    """
    resultado = a**b
    return resultado

def ecuacionSegundoGrado(a,b,c):
    """
    Resuelve una ecuación de segundo grado
    
    Parámetros:
    a (int/float)
    b (int/float)
    c (int/float)
    
    Retorna:
    (tuple | str): Dos resultados (x1, x2) que son las soluciones, o un mensaje de error.
    """
    # Comentario para mí mismo: Si 'a' es cero, no es una ecuación de segundo grado
    # En ese caso no podemos usar la fórmula, así que devolvemos un mensaje.
    if a == 0:
        return "No es una ecuación de segundo grado"
    
    # Aquí usamos la famosa fórmula general para encontrar las dos soluciones.
    
    # Calculamos la primera solución (la de la suma, con el signo +)
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    
    # Calculamos la segunda solución (la de la resta, con el signo -)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

    return x1, x2


if __name__ == "__main__":
    # Esto es el menú para probar las funciones.
    print("1.RAIZ CUADRADA")
    print("2.FACTORIAL")
    print("3.POTENCIA")
    print("4.ECUACIÓN DE SEGUNDO GRADO")
    operacion = int(input("Introduce la operación que desea realizar: "))

    match operacion:
        case(1):
            n = int(input("Introduzca un número para la raiz cuadrada: "))
            print(raizCuadrada(n))
        case(2):
            n = int(input("Introduce un número para el factorial"))
            print(factorial(n))
        case(3):
            a = int(input("Introduzca la base: "))
            b = int(input("Introduzca el exponente: "))
            print(potencia(a,b))
        case(4):
            a = int(input("Introduzca el número 'a': "))
            b = int(input("Introduzca el número 'b': "))
            c = int(input("Introduzca el número 'c': "))
            print(ecuacionSegundoGrado(a,b,c))
        case _:
            print("Opción no válida")