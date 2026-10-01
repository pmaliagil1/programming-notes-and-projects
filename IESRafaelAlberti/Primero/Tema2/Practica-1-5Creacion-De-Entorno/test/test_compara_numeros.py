from src.compara_numeros import compara_numeros

# Una sola función de prueba con multiples aserciones
def test_compara_numeros_multiples_casos():
    
    # --- Casos donde num1 es el mayor ---
    # 1. Positivos
    assert compara_numeros(10, 5) == 10
    # 2. Positivo vs Negativo
    assert compara_numeros(9, -1) == 9
    # 3. Negativos (el más cercano a cero es mayor)
    assert compara_numeros(-2, -5) == -2
    
    # --- Casos donde num2 es el mayor ---
    # 4. Positivos
    assert compara_numeros(3, 8) == 8
    # 5. Negativo vs Positivo
    assert compara_numeros(-10, 5) == 5
    # 6. Cero vs Positivo
    assert compara_numeros(0, 6) == 6
    
    # --- Casos donde son iguales (debe retornar 0) ---
    # 7. Positivos iguales
    assert compara_numeros(7, 7) == 0
    # 8. Negativos iguales
    assert compara_numeros(-4, -4) == 0
    # 9. Cero iguales
    assert compara_numeros(0, 0) == 0