from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']


#def zipper(lista1, lista2):
#    intervalo_maximo = (min(len(lista1), len(lista2)))
 #   return [
#        (lista1[i], lista2[i]) for i in range(intervalo_maximo)
#    ]

#print(zipper(cidades, estados))

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))