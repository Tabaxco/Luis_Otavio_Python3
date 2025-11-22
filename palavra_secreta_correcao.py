palavra_secreta = 'perfume'
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = str(input('Digite uma letra: '))
    tentativas += 1

    if len(letra_digitada) > 1:
        print('DIGITE APENAS UMA LETRA')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(f'Palavra formada: {palavra_formada}')


    if palavra_formada == palavra_secreta:
        print('Você ganhou, parabéns!')
        print(f'A palavra era {palavra_formada}')
        print(f'Tentativas: {tentativas}')