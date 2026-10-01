def compara_numeros(num1, num2):
    """
    Recibe dos números y retorna el mayor.
    Retorna 0 si los números son iguales.
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:  # Esto se ejecuta si num1 es igual a num2
        return 0