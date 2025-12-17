caminho_arquivo = '/home/tabaxco/Projetos/Luis_Otavio_Python3/'
caminho_arquivo += 'aula188.txt'

#try:
#    arquivo = open(caminho_arquivo, 'w')
#
#except FileNotFoundError:
#    print('Arquivo não encontrado.')
#
#finally:
#    arquivo.close()


with open(caminho_arquivo, 'w') as arquivo:
    print('Olá mundo')
    print('Arquivo fechado!')