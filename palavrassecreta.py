from random import randint

palavras = ['banana', 'jonas', 'joao', 'roxo']
secreta = randint(0, len(palavras) -1)
palavra_secreta = palavras[secreta]
tentativas = 0
letras_acertadas = []
palavraf = ''

print('Olá! Bem vindo ao jogo da Palavra Secreta!')
print('Você deve adivinhar a palavra!')

while True:
    chute = input('\nDigite uma letra: ').lower()

    if chute == palavra_secreta:
        break

    if chute in palavra_secreta:
        print(f'{chute} está na palavra!')

        if palavra_secreta.count(chute) > letras_acertadas.count(chute) and chute in letras_acertadas:
            print(f'Há mais de uma letra "{chute}" na palavra!')
            letras_acertadas.append(chute)
        
        elif palavra_secreta.count(chute) == letras_acertadas.count(chute):
            print('Já encontrou todas as vezes que essa letra aparece!')

        if chute not in letras_acertadas:
            letras_acertadas.append(chute)
        

        print(letras_acertadas)
    else:
        print('*')

    tentativas += 1

    qtde = len(palavra_secreta)
    print(f'Sua palavra formatada é {'*'*qtde}')
    
    if len(chute) > 1:
        print('\nDIGITE APENAS UMA LETRA!\n')
        continue

print(f'Você acertou! A palavra era {palavra_secreta}\
 você utilizou {tentativas} tentativas!')