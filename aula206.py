class Pessoa:
    ANO_ATUAL = 2025

    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ano_atual = 100
    
    def get_ano_nascimento(self):
        return( f'{Pessoa.ANO_ATUAL=} - {self.idade=}')

Guilherme = Pessoa('Guilherme', 18)
Guilherme.ANO_ATUAL = 2026
print(Guilherme.ANO_ATUAL)
print(Guilherme.get_ano_nascimento())
print(Pessoa.ANO_ATUAL)