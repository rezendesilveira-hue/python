#Faça um programa que peça a temperatura em graus Fahrenheit, 
#Transforme e mostre a temperatura em graus Celsius.
grau_f = float(input('Digite o grau em Fahrenheit: '))
grau_c = 5 * ((grau_f - 32) /9)
print(f'O grau em celsius é: {grau_c :.2f}')