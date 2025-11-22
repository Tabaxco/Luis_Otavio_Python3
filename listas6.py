listacria = []

while True:
    print('Selecione uma opção')
    opc = (input('[I]nserir [A]pagar [L]istar: ')).lower()

    if opc == 'i':
        inserir = input('Valor: ')
        listacria.append(inserir)

    elif opc == 'l':
        for item in enumerate(listacria):
            print(item)

    elif opc == 'a':
        try:
            apagar = int(input('Escolha o indíce para apagar: '))
            listacria.pop(apagar)
        except:
            print('Indíce não existe.')
            continue



