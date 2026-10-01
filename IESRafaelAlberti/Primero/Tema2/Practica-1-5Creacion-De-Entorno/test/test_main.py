# tests/test_main.py
import pytest # Necesario para usar la marca parametrize [cite: 198, 236]
from src.main import suma

# Esta es la prueba que ya tenías
def test_suma():
    assert suma(1, 1) == 2
    assert suma(0, 0) == 0
    assert suma(100, -100) == 0

# Nueva función de prueba parametrizada
@pytest.mark.parametrize(
    "input_n1, input_n2, expected", # Nombres de los parámetros a pasar a la función [cite: 215]
    [ # Lista de tuplas: (número 1, número 2, resultado esperado) [cite: 217]
        (1, 1, 2),    # Caso 1 [cite: 219]
        (0, 0, 0),    # Caso 2 [cite: 221]
        (100, 100, 200), # Corregido de la fuente (la fuente tiene un error tipográfico)
        (-15, -1, -16), # Caso 4 [cite: 226]
        (-3, 8, 5),     # Caso 5 [cite: 228]
        (9, suma(-1,-2), 6) # Caso 6: Prueba con una llamada anidada [cite: 230]
    ]
)
def test_suma_params (input_n1, input_n2, expected):
    # Por cada tupla de arriba, se ejecuta esta aserción [cite: 235]
    assert suma(input_n1, input_n2) == expected
