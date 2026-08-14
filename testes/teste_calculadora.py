from ex09_calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(5, 3) == 8

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar_e_dividir():
    assert multiplicar(4, 3) == 12
    assert dividir(12, 3) == 4
