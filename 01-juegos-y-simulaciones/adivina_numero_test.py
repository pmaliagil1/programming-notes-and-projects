import pytest
from adivina_numero import AdivinaNumero

@pytest.fixture
def juego():
    return AdivinaNumero()

def test_acierta_en_primer_intento(juego):
    entradas = [7]
    assert juego.jugar(5, entradas) is True

def test_falla_todos_los_intentos(juego):
    entradas = [1, 2, 3, 4, 5]
    assert juego.jugar(5, entradas) is False

def test_entrada_invalida_seguido_acierto(juego):
    entradas = ["abc", 7]
    assert juego.jugar(5, entradas) is False  