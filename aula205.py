class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando.')
            return

        self.filmando = True
        print(f'{self.nome} está filmando...')
    
    def parar_filmagem(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando')
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar enquanto filma.')
            return
    
        print(f'{self.nome} está fotografando...')
        self.foto = True
    


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
#print(c1.filmando)
#print(c2.filmando)