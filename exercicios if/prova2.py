horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
hora_normal = 15.00
horas_extras = 0
total = 0
pgamento_extra = 0
if horas_trabalhadas <= 44:
    salario_normal = 44 * hora_normal
    print('=============================================================================')
    print('A jornada foi cumprida corretamente')
    print(f'Horas trabalhadas: {horas_trabalhadas:.2f}')
    print('Valor da hora normal: R$ 15,00')
    print('Resultado esperado: 0 horas extras')
    print(f'O salário normal é: {salario_normal:.2f}')
    print('=============================================================================')
else:
    horas_extras = horas_trabalhadas - 44
    total = 15.00 * 1.50
    pagamento_extra = horas_extras * total
    salario_normal = 44 * hora_normal
    salario_total = salario_normal + pagamento_extra
    print('=============================================================================')
    print(f'Horas trabalhadas: {horas_trabalhadas:.2f}')
    print('Valor da hora normal: R$ 15,00')
    print(f'Resultado esperado: {horas_extras:.2f} horas extras a R$ {total:.2f} cada')
    print(f'O valor a ser recebido em dinheiro é: {pagamento_extra:.2f}')
    print(f'O salário normal é: {salario_normal:.2f}')
    print(f'O salário a ser recebido com os extras é de: {salario_total:.2f}')
    print('=============================================================================')