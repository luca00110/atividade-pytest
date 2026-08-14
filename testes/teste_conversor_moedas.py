from ex18_conversor_moedas import converter_dolar

def test_converter_100_reais():
    assert converter_dolar(100, 5) == 20

def test_converter_50_reais():
    assert converter_dolar(50, 5) == 10

def test_converter_zero():
    assert converter_dolar(0, 5) == 0
