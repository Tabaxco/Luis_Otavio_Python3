macaco = list()
monkey= ['jonas', 'jombas', 'monke']
print(monkey[3])

ultimo_valor = monkey.pop(1)
print(ultimo_valor)

monkey.insert(0, 'roldanos')

monkey[0] = 'MONEY' #muda o negócio para MONEY

monkey.clear()
print(monkey)

alabama = [['jonas', 12], ['luana', 18]]

for elemento in alabama:
    print(f'Nome: {elemento[0]}')
    print(f'Idade: {elemento[1]}')
    print()