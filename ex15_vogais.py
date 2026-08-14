def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    quantidade = 0

    for caractere in texto:
        if caractere in vogais:
            quantidade += 1

    return quantidade
