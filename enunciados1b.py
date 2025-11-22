num = str(input('Digite um valor inteiro: ')).strip()
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par.')
    else:
        print(f'O número {num} é ímpar.')
else:
    print('Você não digitou um número inteiro.')