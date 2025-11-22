import os
from time import sleep

lista = []

def showlist():
    if lista:
        for i, n in enumerate(lista):
            print(f"{i} {n}")
    else:
        print("Lista vazia!")

while True:

    print("Selecione uma das opções: ")
    opc = input('[I]nserir [D]eletar [L]er\n').capitalize()

    os.system('clear')

    if opc == "I":
        val = input("Digite o valor a ser inserido: ")
        lista.append(val)
        sleep(5)

    if opc == "D":
        showlist()
        val = int(input("Digite o indíce a ser deletado: "))
        try:
            lista.pop(val)
            print("Valor deletado")
            

        except IndexError:
            print("Indíce fora da lista...")
        except ValueError:
            print("Apenas números inteiros!")
        sleep(5)

    if opc == "L":
        showlist()
        input("")
    
    os.system('clear')