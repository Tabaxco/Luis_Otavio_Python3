texto = 'texto'.__iter__()
print(texto)

jonas = 'jonas'
print(iter(jonas))

joao = iter('joão')
print(joao.__next__())
print(joao.__next__())
print(joao.__next__())
print(next(joao))

'''
Iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez 
next -> me entregue o próximo valor
iter -> me entregue seu iterador
'''

# for letra in texto

textinho = 'Luiz' # Iterável
iteratador = iter(textinho) #iterator

while True:
    try:
        print(next(iteratador), end = '')
    except StopIteration:
        break