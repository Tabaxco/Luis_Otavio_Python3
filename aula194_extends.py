to_do_list = []

deleted = []

while True:
    print("Comandos: listar, desfazer, refazer")
    commands = input("Digite uma tarefa ou comando: ")

    print()

    if commands.lower() not in ('listar', 'desfazer', 'refazer'):
        to_do_list.append(commands)

    if commands.lower() == 'listar':
        print('TAREFAS:')
        for tarefa in to_do_list:
            print(tarefa)

    elif commands.lower() == 'desfazer':
       deleted_one = input('Digite o que deseja remover (precisa estar igual ao que foi inserido na lista): ')
       to_do_list.remove(deleted_one)
       deleted.append(deleted_one)

    elif commands.lower() == ('refazer'):
        for to_do in deleted:
            if to_do not in to_do_list:
                to_do_list.append(to_do)
                deleted.remove(to_do)
                break

    print()