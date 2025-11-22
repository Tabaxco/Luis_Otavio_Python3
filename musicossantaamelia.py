from random import randint

escolhidos = []


musicos = {
    'guitarrista' : ['Guilherme', 'Wesley'],
    'baterista' : ['Roger', 'Luan'],
    'tecladista' : ['Felipe', 'Mano'],
    'baixista' : ['jonathan', 'thomas']
}

vozes = ['Isadorah', 'Esther', 'Guilherme', 'Vitoria', 'Lorrany']

def escolher_musico():
    for instrumento, nomes in musicos.items():
        indice = randint(0, len(nomes) - 1)
        print(f"{instrumento}: {nomes[indice]}")

def escolher_cantor():
    vozes_escolhidas = []
    for nome in vozes:
        indice = randint(0, len(vozes) - 2)
        if vozes[indice] not in vozes_escolhidas:
            vozes_escolhidas.append(vozes[indice])
    print(f'Cantores: {(", ").join(vozes_escolhidas)}')

escolher_musico()
escolher_cantor()