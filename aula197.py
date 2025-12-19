import os

tarefas = []
tarefas_refazer = []

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefas, tarefas_desfazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} foi removida')
    tarefas_desfazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para refazer')
        return
    
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nenhuma tarefa')
        return
    
    print(f'{tarefa=} adicionada na lista de tarefas')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
       'listar' : lambda: listar(tarefas),
       'desfazer' : lambda: desfazer(tarefas, tarefas_refazer),
       'refazer' : lambda: refazer(tarefas, tarefas_refazer),
       'clear' : lambda: os.system('clear'),
       'adicionar' : lambda: adicionar(tarefa, tarefas),
   }
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()