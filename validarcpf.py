CPF = "74682489070"
lista = []
lista2 = []
soma = 0

for num in CPF:
    lista.append(num)

j = 10

for i in range(0, 9):
     lista2.append(int(lista[i]) * j)
     j -= 1

soma = sum(lista2)
multi = soma*10
resto = multi % 11
if resto > 9:
    print("0")
else: 
    print(resto)