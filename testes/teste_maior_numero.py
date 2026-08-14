from ex04_maior_numero import maior_numero

def test_primeiro_maior():
    assert maior_numero(10, 5) == 10

def test_segundo_maior():
    assert maior_numero(3, 8) == 8

def test_numeros_iguais():
    assert maior_numero(6, 6) == 6
