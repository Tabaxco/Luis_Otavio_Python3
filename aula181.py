numero = 5

def fatorial(n):
    if n == 0 or n == 1:
        return n
    return n * fatorial(n - 1)

fatorial_cinco = fatorial(numero)
print(fatorial_cinco)

def recursiva(inicio=0, fim=10):
    if inicio >= fim:
        return fim
    
    print(inicio, fim)
    
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())