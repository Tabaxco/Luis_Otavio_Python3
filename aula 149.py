def generator (n=0, maximum=10):
    #yield 1 # Pausar
    ##return 'ACABOU'
   # print('Continuando')
    #yield 2 # Pausar 2
    #print('Mais uma...')
    #yield 3
    #print('Vou terminar')
    #return 'ACABOU'

    while True:
        yield n

        if n >= maximum:
            return
        
        n += 1

gen = generator(maximum=10000000000)
#print(gen.__iter__())
#print(next(gen))
#print(next(gen))
#print(next(gen))
#print(next(gen))

for n in gen:
    print(n)