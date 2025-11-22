nome = str(input('Qual o seu nome? '))
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
IMC = peso/(altura**2) # ou peso / (altura**2)
print(f'{nome} tem o IMC = {IMC:.1f}, ', end = '') # :,.1f 10004 ficaria 100,4

if IMC <=16.4:
    print('Magreza')
elif 16.4 < IMC <=25.1:
    print('Normal')
elif 25.1 < IMC <= 29.7:
    print('Sobrepeso')
elif 29.7 < IMC:
    print('Obesidade Mórbida.')