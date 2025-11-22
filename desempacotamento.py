nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes
### nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']

nome6 = nomes[1]

nome1, *_ = ['Maria', 'Helena', 'Luiz'] #resto recebe o que sobrou

print(nome6)
print(_)