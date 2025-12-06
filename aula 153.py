try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIU ZERO')
except IndexError as error:
    print(error)
    print('IndexError')
except(NameError, ImportError):
    print('NameError, ImportError')
else:
    print('NÃO DEU ERRO MACACO LOUCO')
finally:
    print('Fechar arquivo')