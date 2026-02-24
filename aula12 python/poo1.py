class Carro:
    def __init__(self, marca: str, modelo: str, ano: int, velocidade_maxima: float):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0
    
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.velocidade_atual} Km/h)'


carro1 = Carro('Fiat', 'Uno', 2010, 100)
print(carro1)
carro1.velocidade_atual = 30
print(carro1)

carro2 = Carro('Chevrolet', 'Celta', 2000, 180)
print (carro2)
carro2.velocidade_atual = 20
print(carro2)
