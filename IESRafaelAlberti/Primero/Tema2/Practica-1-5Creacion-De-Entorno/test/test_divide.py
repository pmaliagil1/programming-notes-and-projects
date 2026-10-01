import pytest
from src.divide import divide

# --- 1. Pruebas de Éxito (Múltiples assert) ---
def test_division_multiples_casos():
    
    # 1. División exacta (10 / 2 = 5.0)
    assert divide(10, 2) == 5.0
    
    # 2. División con resultado decimal. Usamos el valor float preciso de Python.
    assert divide(10, 3) == 3.3333333333333335 
    
    # 3. División con resultado negativo (-10 / 2 = -5.0)
    assert divide(-10, 2) == -5.0
    
    # 4. División de dos negativos (resultado positivo) (-10 / -5 = 2.0)
    assert divide(-10, -5) == 2.0
    
    # 5. Dividir cero entre un número (0 / 5 = 0.0)
    assert divide(0, 5) == 0.0

# --- 2. Prueba de Fallo Esperado (Excepción) ---
def test_division_por_cero_lanza_excepcion():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)