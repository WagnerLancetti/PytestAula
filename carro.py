class Carro():
    # CONSTRUTOR
    def __init__(self,Marca=None,Placa=None,Cor=None,Ano=-1): # Construtor padrao e com parametros de entrada
        self.Marca = Marca
        self.Placa = Placa
        self.Cor = Cor
        self.Ano = Ano

    @classmethod
    def from_dict(cls, d):
        return Carro(**d)

    def specialized_car(self, typecar):
        self.Marca = f"{typecar} {self.Marca}"