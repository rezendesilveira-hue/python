salario = float(input('Digite o salário do funcionário: '))
percentual20 = 0.20
percentual15 = 0.15
percentual10 = 0.10
percentual5 = 0.05

if salario <= 280.00:
    print(f'Salário atual: {salario :.2f}')
    print('O percentual de aumento é de 20%')
    aumento = salario * percentual20
    print(f'O aumento é de: {aumento :.2f}')
    novosal = salario + aumento
    print(f'O novo salário é: {novosal :.2f}')     
elif salario > 280.00 and salario <= 700.00:
    print(f'Salário atual: {salario :.2f}')
    print('O percentual de aumento é de 15%')
    aumento = salario * percentual15
    print(f'O aumento é de: {aumento :.2f}')
    novosal = salario + aumento
    print(f'O novo salário é: {novosal :.2f}')     
elif salario > 700.00 and salario <= 1500.00:
    print(f'Salário atual: {salario}')
    print('O percentual de aumento é de 10%')
    aumento = salario * percentual10
    print(f'O aumento é de: {aumento :.2f}')
    novosal = salario + aumento
    print(f'O novo salário é: {novosal :.2f}') 
elif salario > 1500.00:
    print(f'Salário atual: {salario}')
    print('O percentual de aumento é de 5%')
    aumento = salario * percentual5
    print(f'O aumento é de: {aumento :.2f}')
    novosal = salario + aumento
    print(f'O novo salário é: {novosal :.2f}')

