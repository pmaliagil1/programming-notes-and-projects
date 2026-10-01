from src.ecuacion_segundo_grado import ecuacionSegundoGrado

def test_ecuacion_segundo_grado_casos_completos():
    

    resultado_1 = ecuacionSegundoGrado(1, -5, 6)
    assert set(resultado_1) == {2.0, 3.0}


    resultado_2 = ecuacionSegundoGrado(1, -7, 12)
    assert set(resultado_2) == {3.0, 4.0}

    resultado_3 = ecuacionSegundoGrado(1, 0, -9)
    assert set(resultado_3) == {-3.0, 3.0}
    

    resultado_4 = ecuacionSegundoGrado(1, -2, 1)
    assert set(resultado_4) == {1.0}

    assert ecuacionSegundoGrado(0, 5, 6) == "No es una ecuación de segundo grado"


    assert ecuacionSegundoGrado(1, 0, 1) == (None, None)