#Faça um programa que leia uma lista de 5 números inteiros e mostre-os individualmente.
num = []
qtde = 5

for numero in range(qtde):
    num_novo = int(input(f'Digite o {numero + 1}º número: '))
    num.append(num_novo)
print('Números: ')

for num_novo in num:
    print(f' - {num_novo}')