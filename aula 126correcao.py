perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1', '3', '4', '5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['25', '55', '10', '51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2',
        'Opções' : ['4', '5', '2', '1'],
        'Resposta' : '5',
    },
]
qtde_acertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
        print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    int_escolha = None
    qtde_opcoes = len(opcoes)

    if escolha.isdigit():
        int_escolha = int(escolha)

    if int_escolha is not None:
        if int_escolha >= 0 and int_escolha < qtde_opcoes:
            if opcoes[int_escolha] == pergunta['Resposta']:
                acertou = True
    print()
    if acertou:
        print('Acertou')
        qtde_acertos += 1

    else:
        print('Errou')

    print()

print('Você acertou', qtde_acertos)
print('de', len(perguntas), 'perguntas')