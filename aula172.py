lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def somador(lista1, lista2):
    intervalo_maximo = min(len(lista_a), len(lista_b))
    return [
        lista1[i]+lista2[i] for i in range(intervalo_maximo)
    ]

lista_soma = somador(lista_a, lista_b)
print(lista_soma)