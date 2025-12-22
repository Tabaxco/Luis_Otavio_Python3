#string = 'Luiz'
#print(string.upper())
#print(isinstance(string, str))

class Pessoa:
    def __init__ (self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


jonas = Pessoa('Guilherme', 'Leite')
#jonas.nome = 'Guilherme'
#jonas.sobrenome = 'Leite'

Nycollas = Pessoa('Nicolas', 'Ferreira')
#Nycollas.nome = 'Nicolas'
#Nycollas.sobrenome = 'Ferreira'

print(jonas.nome)
print(jonas.sobrenome)

print(Nycollas.nome)
print(Nycollas.sobrenome)