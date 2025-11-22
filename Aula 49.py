

macaco = input('Fala um número e eu dobro nat au cara: ')

#macaco_float = float(macaco)


#print(macaco.isdecimal())
#print(f'O dobro de {macaco} é {macaco_float*2:.2f}')

try:
    macaco_float = float(macaco)
    print(f'O dobro de {macaco} é {macaco_float*2:.2f}')
except:
    print('Isso não é um número.')