tempo_servico = float(input('Digite o tempo de serviço em anos: '))

if tempo_servico > 1:
    valor_fgts = float(input('Digite o valor do FGTS: '))
    resultado = (valor_fgts *40) / 100
    print(f'Tempo de serviço: {tempo_servico}')
    print(f'Valor do Fgts: {valor_fgts}')
    print(f'O valor a ser pago do FGTS é: {resultado}')
else:
    print('Não tem multa de 40% a ser paga')
