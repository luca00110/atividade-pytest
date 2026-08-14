from ex19_validar_senha import validar_senha

def test_senha_valida():
    assert validar_senha("12345678") == "Senha válida"

def test_senha_invalida():
    assert validar_senha("1234567") == "Senha inválida"

def test_senha_com_letras():
    assert validar_senha("Senha123") == "Senha válida"
