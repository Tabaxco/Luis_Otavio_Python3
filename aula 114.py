def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

def complexo(x):
    if (x % 2 == 0):
        return f'{x} é par'
    return f'{x} é ímpar'

resultado = multi(3, 6)
print(resultado)

oquee = complexo(resultado)
print(oquee)