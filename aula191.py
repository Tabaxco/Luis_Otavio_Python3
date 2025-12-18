import os

caminho_arquivo = '/home/tabaxco/Projetos/Luis_Otavio_Python3/'
caminho_arquivo += 'aula191.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    arquivo.write('Atenção') 

os.unlink(caminho_arquivo) #Apaga o arquivo
os.remove(caminho_arquivo)

os.rename(caminho_arquivo, 'aula191_2.txt')