while True:
    try:
            nome = input('Digite seu nome: ')
            if not nome.isalpha():
                   raise ValueError('Nome inválido')
            print(f'Olá, {nome}!')
            break
    except ValueError as e:
            print(e)
            continue
    break