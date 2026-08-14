from ex11_classificar_numero import classificar_numero

def test_positivo():
    assert classificar_numero(10) == "Positivo"

def test_negativo():
    assert classificar_numero(-10) == "Negativo"

def test_zero():
    assert classificar_numero(0) == "Zero"
