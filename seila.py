indice = 0
nome = "Guilherme Leite Rodrigues"
macaco = ''

while indice < len(nome):
    print(nome[indice])
    macaco += f'{nome[indice]}*'
    indice += 1

print(macaco)