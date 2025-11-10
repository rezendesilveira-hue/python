#Faça um programa que peça um numero para o usuário, e mostre na tela o fatorial desse numero.
num = int(input('Digite um numero: '))
fatorial = 1

for n in range(1, num +1):
    fatorial *= n

print(f'O fatorial de {num} é {fatorial}')