from aula207_a import Pessoa
import json

with open ('aula207.json', 'r') as arquivo:
    dados_do_joao = json.load(arquivo)
    print(dados_do_joao)
    p1 = Pessoa(**dados_do_joao)
    print(vars(p1))