lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
]

def encontraduplicado(lista_de_lista_de_inteiros):
    for lista in lista_de_listas_de_inteiros:
        nums = set()
        duplicados = None
        listados = []
        print(lista)
        for i, v in enumerate(lista):
            if v not in nums:
                nums.add(v)
            else:
                duplicados = v
                print(f"{v} é duplicado!")
                break
            
            if len(nums) == len(lista):
                print(-1)
    
print(encontraduplicado(lista_de_listas_de_inteiros))