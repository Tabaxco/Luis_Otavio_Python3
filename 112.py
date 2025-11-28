x, y, *resto = 1, 2, 3, 4

print(x, y, *resto)


def soma(*args):
    total = 0
    x = 1
    # args = list(args)
    #return sum(args)
    #return args[1] + args[2]
    for numero in args:
        total += numero
    return total, x

jonas, bonas = soma(2, 1)
print(soma(1, 2, 3))
print(sum((1, 2)))