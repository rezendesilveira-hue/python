def formatar_peso(peso):
    return f'{peso:.2f} KG'

def formatar_altura(altura):
    return f'{altura:.2f} Metros'

def calcular_imc(peso, altura):
    return peso / (altura * altura)


imc = calcular_imc(peso = 76.8, altura = 1.71)
print(f'O usuario tem {formatar_peso} e imc {imc}')