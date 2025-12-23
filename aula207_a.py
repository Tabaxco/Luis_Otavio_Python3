class Pessoa:
    def __init__(self, nome, idade, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

dados_do_joao = '{"nome" : "João", "idade": 19, "nacionalidade": "brasileiro"}'

with open ('aula207.json', 'w+') as arquivo:
    arquivo.write(dados_do_joao)