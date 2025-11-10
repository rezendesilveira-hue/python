#Calculador de Média: Peça ao usuário 3 valores decimais, e mostre a média aritimética (a soma dos valores dividido pela quantidade) dos numeros
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
media = (num1 + num2 + num3) / 3
print (f'O resultado da média é: {media:.2f}')