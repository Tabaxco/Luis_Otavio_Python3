def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1=adiciona_clientes('guilherme')
adiciona_clientes('Joana', cliente1)

cliente2=adiciona_clientes('macaco')
adiciona_clientes('Miquinho', cliente2)

print(cliente1)
print(cliente2)