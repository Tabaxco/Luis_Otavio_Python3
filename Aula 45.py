variavel = 'ABC'

print (f'{variavel: >10}')
print (f'{variavel: <10}')
print (f'{variavel: ^10}')
print(f'{variavel:0^10}') #não pode dar espaço
print(f'{variavel:$^10}')
print(f'{10000.00000095:.1f}')
print(f'{10000.00000095:,.1f}')
print(f'{-10000.00000095:,.1f}')
print(f'{10000.00000095:+,.1f}')
print(f'{10000.00000095:0>+10,.1f}')
print(f'{10000.00000095:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')