p1 = {
    'nome' : "luiz",
    'sobrenome' : "miranda",
}

# print(p1.get('nome'))
#p2 = p1.get('nome', None)
# print(p1['nome'])

#if p2:
   # print(p2)
#else:
   # print('Não Existe')

#nome = p1.pop('nome')
#print(nome)

#ultima_chave = p1.popitem()
#print(ultima_chave)
#print(p1)
#p1.update({
#    'nome' : 'unova',
#    'idade': 30,
#
#})
#p1.update(nome='umnovo dia', idade = 30)
tuplinha = (('nome', 'novo valor'), ('idade', 30))
lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(lista)
print(p1)