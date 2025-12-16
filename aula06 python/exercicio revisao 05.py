def calcular_imc(peso, altura):
    return peso / (altura * altura)


imc = calcular_imc(peso = 76.8, altura = 1.71)
print(f'O usuario tem o imc {imc:.2f}')