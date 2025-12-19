caminho_arquivo = '/home/tabaxco/Projetos/Luis_Otavio_Python3/'
caminho_arquivo += 'aula189.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    
    arquivo.seek(0,0)
    print(arquivo.read())
    arquivo.seek(0,0)
    print(arquivo.readline())
    print(arquivo.readline().strip())
    print(arquivo.readline(), end = '')

    arquivo.seek(0,0)
    for linha in arquivo.readlines():
            print(linha.strip())
    

print('#' * 40)

with open(caminho_arquivo,'r') as arquivo:
    print(arquivo.read())