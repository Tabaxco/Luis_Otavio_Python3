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

points = 0
respostas = [2, 0, 2]
indice_resposta = 0

for dic in perguntas:
    for k, v in dic.items():
        i = 0
        if k == 'Pergunta':
            print(f"{k}:", v)
        elif k == 'Opções':
            print(f'{k}:')
            for resp in v:
                print(f'{i}) {v[i]}')
                i += 1
    escolha = int(input('Escolha uma opção: '))

    if escolha == respostas[indice_resposta]:
        print("Você acertou!")
        points += 1
    else:
        print('Você errou!')
    
    print("")
    indice_resposta += 1



print(f'Você acertou {points} perguntas de {len(perguntas)} perguntas')