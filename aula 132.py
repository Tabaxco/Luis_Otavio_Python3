letras = set()
while True:
    letra = input('Digite: ').lower()

    if letra.isalpha():
        letras.add(letra)
    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)