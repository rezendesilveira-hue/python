
# 1 importar o mudulo todo precisa referenciar o modulo depois a função
import operacoes 

# importando as funcoes somente, não precisa referenciar o modulo
#from operacoes import somar, subtrair, multiplicar, dividir 

#import operacoes as op /// importando modulo e colocando apelido, ai fica op.somar...


# Código Principal
print('=' * 20)
print('Calculadora: ')
print('[1] - Somar')
print('[2] - Subtrair')
print('[3] - Multiplicar')
print('[4] - Dividir')
print('=' * 20)

opcao = input('Digite uma opção: ')

if opcao == '1':
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    resultado = operacoes.somar(num1, num2)

    print(f'O resultado da soma é: {resultado}')

elif opcao == '2':
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    resultado = operacoes.subtrair(num1, num2)

    print(f'O resultado da subtração é: {resultado}')

elif opcao == '3':
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    resultado = operacoes.multiplicar(num1, num2)

    print(f'O resultado da multiplicação é: {resultado}')

elif opcao == '4':
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    resultado = operacoes.dividir(num1, num2)

    if resultado != None:
        print(f'O resultado da divisão é: {resultado}')
    else:
        print('Você não pode dividir um numero por 0.')
else:
    print('Opção Inválida.')
