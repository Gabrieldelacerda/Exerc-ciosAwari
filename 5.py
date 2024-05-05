def contar_vogais(palavra):
    vogais = 'aeiouAEIOU'
    quantidade_vogais = 0
    for letra in palavra:
        if letra in vogais:
            quantidade_vogais += 1
    return quantidade_vogais

palavra = input('Digite uma palavra: ')
print(f'A quantidade de vogais na palavra {palavra} é {contar_vogais(palavra)}')