import json

with open('aula192.json', 'r') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa['nome'])