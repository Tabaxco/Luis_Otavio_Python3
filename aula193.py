def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista

cliente1=adiciona_clientes('guilherme')
adiciona_clientes('Joana', cliente1)
cliente2=adiciona_clientes('macaco')

print(cliente1)