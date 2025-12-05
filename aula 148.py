import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem __inter e __next__

lista = [n for n in range(10)]
generator = (n for n in range(10000000)) #não dá pra acessar os indices, len() porque não está na memória
#generator só sabe qual o seu próximo valor

# print(lista)
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))

for n in generator:
    print(n)