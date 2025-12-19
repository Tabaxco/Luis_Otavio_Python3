#def soma(x, y, /):
#    print(x + y)

def soma(a, b, /, *, c):
    print(a + b)

soma(1, 2, c=3)

