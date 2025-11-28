#pessoa = {'nome' : 'Guilherme',
          #'sobrenome' : 'Leite',
          #'idade' : 18}

#pessoas = dict(nome='Guilherme Leite', 
               #sobrenome='Miranda')

pessoa = {
    'nome' : 'Guilherme Leite',
    'sobrenome' : 'Rodrigues',
    'idade' : '18',
    'altura' : '1.77',
    'endereços' : [
        {'rua' : 'tal tal', 'número': 12},
        {'rua' : 'jonas mago', 'number': 15},
    ],
}
 
for chave in pessoa:
    print(chave, pessoa[chave])