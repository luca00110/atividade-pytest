from ex16_tabuada import tabuada

def test_tabuada_do_cinco(capsys):
    tabuada(5)
    saida = capsys.readouterr().out
    assert "5 x 1 = 5" in saida
    assert "5 x 10 = 50" in saida

def test_tabuada_do_zero(capsys):
    tabuada(0)
    saida = capsys.readouterr().out
    assert "0 x 1 = 0" in saida

def test_tabuada_do_dois(capsys):
    tabuada(2)
    saida = capsys.readouterr().out
    assert "2 x 5 = 10" in saida
