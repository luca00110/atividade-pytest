from ex10_imc import calcular_imc

def test_imc_exato():
    assert calcular_imc(70, 1.75) == 70 / (1.75 ** 2)

def test_imc_peso_maior():
    assert calcular_imc(100, 2) == 25

def test_imc_peso_menor():
    assert calcular_imc(50, 1.5) == 50 / (1.5 ** 2)
