from ex12_potencia import potencia

def test_potencia_basica():
    assert potencia(2, 3) == 8

def test_expoente_zero():
    assert potencia(5, 0) == 1

def test_base_zero():
    assert potencia(0, 5) == 0
