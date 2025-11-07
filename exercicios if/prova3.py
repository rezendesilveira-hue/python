print('===============================================================')
salario_mensal = float(input('Digite o salario mensal: '))
meses_trabalhados = float(input('Digite os meses trabalhados: '))
print('===============================================================')

while meses_trabalhados != 0:
    ferias_proporcionais = (salario_mensal / 12) * meses_trabalhados
    print('===============================================================')
    print(f'Salario mensal é de: {salario_mensal:.2f}')
    print(f'Meses trabalhados são: {meses_trabalhados}')
    print(f'Férias proporcionais são: {ferias_proporcionais:.2f}')
    salario_mensal = float(input('Digite o salario mensal: '))
    meses_trabalhados = float(input('Digite os meses trabalhados: '))
    print('===============================================================')
    
print('Não tem calculos a fazer')