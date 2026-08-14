from ex01_saudacao import saudacao

def test_saudacao_nome():
    assert saudacao("João") == "Olá, João! Seja bem-vindo."

def test_saudacao_nome_diferente():
    assert saudacao("Maria") == "Olá, Maria! Seja bem-vindo."

def test_saudacao_vazio():
    assert saudacao("") == "Olá, ! Seja bem-vindo."
