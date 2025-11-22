frase = 'Python é uma lingaugem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido Van Rossum'.lower()

maiorl = ''
qtde_aparecel = 0

for i in range (len(frase)):
    letra_atual = frase[i]
    quantidade_letra = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if qtde_aparecel <= quantidade_letra:
        qtde_aparecel = quantidade_letra
        maiorl = letra_atual

    print(letra_atual, quantidade_letra)
    i += 1

print(f'A letra que apareceu mais vezes foi "{maiorl}" que apareceu {qtde_aparecel} vezes')