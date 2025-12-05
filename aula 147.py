iterable = ['Eu', 'Tenho', '__iter__']
#iterator = iterable.__iter__() #tem __inter e __next__
iterator = iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
