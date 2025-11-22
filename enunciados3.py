while True:
    try:
        usuario = str(input('Digite o seu nome de usuário: ')).strip()
        caracteres = len(usuario)
    except ValueError:
        print('Usuário inválido. Tente novamente.')
        continue
    else:
        if caracteres <= 4:
            print('Seu nome é curto.')
        elif caracteres <= 6:
            print('Seu nome é normal.')
            break
        else:
            print('Seu nome é muito grande.')
            break
print(f'Seja bem vindo {usuario}!')