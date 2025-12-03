#lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
#lista2 = sorted(lista)
#lista.sort(reverse=True)
#print(lista)
#print(lista2)

lista = [
    {'nome' : 'Luiz', 'sobrenome' : 'miranda'},
    {'nome' : 'Maria', 'sobrenome' : 'Oliveira'},
    {'nome' : 'Daniel', 'sobrenome' : 'Silva'},
    {'nome' : 'Eduardo', 'sobrenome' : 'Morereira'},
    {'nome' : 'Aline', 'sobrenome' : 'Souza'},
]

#def ordena(item):
#    print(item)
 #   return item['nome']

#lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)