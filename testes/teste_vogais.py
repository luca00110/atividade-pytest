from ex15_vogais import contar_vogais

def test_contar_vogais():
    assert contar_vogais("Python") == 1

def test_todas_as_vogais():
    assert contar_vogais("aeiou") == 5

def test_sem_vogais():
    assert contar_vogais("rhythm") == 0
