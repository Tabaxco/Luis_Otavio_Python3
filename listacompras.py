import os
from time import sleep

lista = []


def showlist():
    if lista:
        print(", ".join(lista))
    else:
        print("Lista vazia!")

while True:

    print("Selecione uma das opções: ")
    opc = input('[I]nserir [D]eletar [L]er\n').capitalize()

    if opc == "I":
        val = input("Digite o valor a ser inserido: ")
        lista.append(val)
        sleep(5)

    if opc == "D":
        print("")
        showlist()
        val = int(input("Digite o valor a ser deletado: "))
        try:
            lista.pop(val)
            print("Valor deletado")
            sleep(5)

        except:
            print("Indíce fora do limite...")


    if opc == "L":
        showlist()
        input("")
    
    os.system('clear')