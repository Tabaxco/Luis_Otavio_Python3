import copy

produtos = [
    {'nome' : 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco':10.11},
    {'nome': 'Produto 2', 'preco' : 105.87},
    {'nome' : 'Produto 4', 'preco': 69.90},
]

novos_produtos = copy.deepcopy(produtos)
for dict in novos_produtos:
    for c, v in dict.items():
        dict['preco'] += (round(dict['preco'] * 0.10, 2))

print(*novos_produtos, sep='\n')
print()

produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key = lambda produto: produto['nome'], reverse=True)
print(*produtos_ordenados_por_nome, sep='\n')

print()

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_preco, key = lambda produto: produto['preco'])
print(*produtos_ordenados_por_preco, sep='\n')
print()
