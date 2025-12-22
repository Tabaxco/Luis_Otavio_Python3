class Carro:
    def __init__(self, nomelouco='Marea'):
        self.nome = nomelouco
    
    def acelerar(self) -> None:
        print(f'{self.nome} está louco!')

fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)
#print(fusca.nome)

celta = Carro('Celta')
#print(celta.nome)

marea = Carro()
#print(marea.nome)

#fusca.acelerar()