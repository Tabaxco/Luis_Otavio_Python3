CPF = "74682489070"
lista = []
lista2 = []
soma = 0
resultado = 0

for num in CPF:
    lista.append(num)

j = 11

for i in range(0, 9):
     resultado = int(lista[i]) * j
     lista2.append(resultado)
     j -= 1
     if i == 8:
        lista2.append(int(lista[0]) * j)


soma = sum(lista2)
multi = soma*10
resto = multi % 11
if resto > 9:
    print("0")
else: 
    print(resto)