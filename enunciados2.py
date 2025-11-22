
cumprimento = None

while True:
    try:
        horas = int(input('Que horas são? '))
        if horas < 0 or horas > 23:
            raise ValueError('Hora inválida.')
        minutos = int(input('Quantos minutos? '))
        if minutos <0 or minutos > 59:
            raise ValueError('Minuto inválido.')
        break
    except ValueError as e:
        print('O horário está incorreto.')
        continue


if horas <= 12:
    cumprimento = 'Bom dia!'
elif horas <= 18:
    cumprimento = 'Boa tarde!'
else:
    cumprimento = 'Boa noite!'

print(f'Agora são {horas}:{minutos}. {cumprimento}')