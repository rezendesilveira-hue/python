#Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

#O produto do dobro do primeiro com metade do segundo .
#A soma do triplo do primeiro com o terceiro.
#O terceiro elevado ao cubo.
int1 = int(input('Digite um número inteiro: '))
int2 = int(input('Digite o segundo número inteiro: '))
real = float(input('Digite um número real: '))
dobro = (int1 * 2) * (int2 / 2)
triplo = (int1 * 3) + real
soma = triplo + real    
elevado = real ** 3
print(f'O produto do dobro do primeiro com metade do segundo é: {dobro}')
print(f'A soma é: {soma}')
print(f'O terceiro elevado ao cubo é: {elevado :.2f}')
