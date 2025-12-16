def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return None
    return n1 / n2 

def numeros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    return num1, num2

print('=' *30)
print('Calculadora')
print('[1] - Somar')
print('[2] - Subtratir')
print('[3] - Multiplicar')
print('[4] - Dividir')
print('=' *30)

opcao = input('Digite uma opção: ')

if opcao == '1':
   num1, num2 = numeros() # tuplas
   resultado = somar(num1, num2)
   print(f'O resultado de {num1} + {num2} = {resultado}')
elif opcao == '2':
    num1, num2 = numeros()
    resultado = subtrair(num1, num2)
    print (f'O resultado de {num1} - {num2} = {resultado}')
elif opcao == '3':
    num1, num2 = numeros()
    resultado = multiplicar(num1, num2)
    print(f'O resultado de {num1} * {num2} = {resultado}')
elif opcao == '4':
    num1, num2 = numeros()
    resultado = dividir(num1, num2)
    print(f'O resultado de {num1} / {num2} = {resultado}')
else:
    print('Opção errada')       
    
       
