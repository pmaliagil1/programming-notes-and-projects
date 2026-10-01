"""1. Manejo de Excepciones Básico: Crea un programa que pida un número entero al
usuario. Utiliza un bloque try-except para capturar la excepción ValueError si el
usuario introduce texto e informa del error sin que el programa rompa.
"""

try:
    entero = int(input("Introduce un entero: "))
    print(entero)


except ValueError:
    print("Entrada no válida")
except Exception as e:
    print(f"Algo ha salido mal: {e}")
    