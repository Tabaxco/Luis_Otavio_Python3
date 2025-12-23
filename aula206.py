class Pessoa:
    ANO_ATUAL = 2025

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100
    
    def get_ano_nascimento(self):
        return( f'{Pessoa.ANO_ATUAL=} - {self.idade=}')

dados = {'nome':'João', 'idade': 36}
p1 = Pessoa(**dados)

#p1 = Pessoa('kalel', 35)
#p1.nome = 'Eita'
#del p1.nome
#print(p1.__dict__)
print(vars(p1))