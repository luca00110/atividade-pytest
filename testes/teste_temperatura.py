from ex05_temperatura import celsius_para_fahrenheit

def test_zero_celsius():
    assert celsius_para_fahrenheit(0) == 32

def test_cem_celsius():
    assert celsius_para_fahrenheit(100) == 212

def test_temperatura_negativa():
    assert celsius_para_fahrenheit(-40) == -40
