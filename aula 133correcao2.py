lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # 1. Sem duplicados
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],  # 2. O primeiro duplicado é o 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
]

def encontraduplicado_corrigido(lista_de_listas):
    # Loop principal: itera sobre cada lista dentro da lista de listas
    for lista in lista_de_listas:
        nums = set()
        print(lista) # Imprime a lista sendo processada
        
        # Loop interno: itera sobre os valores da lista atual
        for v in lista:
            if v in nums:
                # Duplicado encontrado! Retorna e TERMINA a função.
                return(f"{v} é duplicado!")
            else:
                # Adiciona o número ao set para rastreamento
                nums.add(v)
    
    # Se o loop principal terminar sem encontrar nenhum duplicado em NENHUMA lista, 
    # o código chega aqui.
    return(-1)

print(encontraduplicado_corrigido(lista_de_listas_de_inteiros))