def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joao', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))



#s1 = criar_saudacao('Bom dia', 'Luiz')
#s2 = criar_saudacao('Boa noite', 'Luiz')
#print(s1('Luiz'))
#print(s2('Luiz'))