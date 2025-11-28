pessoa = {}

chave = 'nome_completo'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'
lista = []

del pessoa['sobrenome']


#print(pessoa.get('sobrenome', None))
if pessoa.get('sobrenome') is not None:
    print(pessoa['sobrenome'])
else:
    print('Não existe')

#try:
 #   print(pessoa['sobrenome'])
#except:
 #   print('Não existe')
#finally:
 #   print("Bibinos")


     