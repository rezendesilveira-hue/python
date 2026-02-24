carro_uno = {
    'marca': 'Fiat',
    'modelo': 'Uno',
    'velocidade' : 0,
    'velocidade_maxima': 180
}
carro_celta = {
    'marca': 'Chevrolet',
    'modelo': 'Celta',
    'velocidade' : 0,
    'velocidade_maxima': 200
}

def acelerar (carro, velocidade):
    carro['velocidade'] += 20

def frear(carro, velocidade):
    carro['velocidade'] -+ velocidade

print(carro_uno)
acelerar(carro_uno, velocidade=20)
print(carro_uno)

print(carro_celta)
acelerar(carro_celta, velocidade=30)
print(carro_celta)