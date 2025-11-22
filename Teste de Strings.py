
nome = str(input('Digite o seu nome: ')) or None
idade = int(input('Digite a sua idade: ')) or None

if nome != None and idade != None:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do teu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
