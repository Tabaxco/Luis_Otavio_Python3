string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print('upado')
    print(getattr(string, metodo()))
else:
    print('Não existe o método', metodo)