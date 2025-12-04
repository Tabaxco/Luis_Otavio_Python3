produto = {
    'nome' : 'Caneta Azul',
    'preco' : 2.5,
    'categoria' : 'Escritório',
}


#dc = {
#    chave : valor
#    if isinstance(valor, (int, float)) else valor.upper()
#    for chave, valor 
#    in produto.items()
#}


#dc = {
#    chave : valor.upper()
#   if isinstance(valor, str) else valor 
#    for chave, valor 
#    in produto.items()
#    if chave == 'categoria'
#}

dc = {
    chave : valor.upper()
    if isinstance(valor, str) else valor 
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b')
]

#dc = {
#    chave : valor
#    for chave, valor 
#    in lista
#}


print(dict(dc))


s1 = {i**2 for i in range(10)}
#print(set(range(10)))
print(s1)
tupperware = (i **2 for i in range(10))
print(tupperware)

for num in tupperware:
    print(num)