from ex20_cadastrar_produto import cadastrar_produto

def test_produto_formatado():
    resultado = cadastrar_produto("Mouse Gamer", 89.90, 15)
    assert "Produto: Mouse Gamer" in resultado

def test_preco_formatado():
    resultado = cadastrar_produto("Teclado", 150, 10)
    assert "Preço: R$ 150.00" in resultado

def test_estoque_formatado():
    resultado = cadastrar_produto("Monitor", 800, 5)
    assert "Estoque: 5 unidades" in resultado
