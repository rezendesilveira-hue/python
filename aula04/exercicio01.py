#Faça um programa que peça um numero positivo para o usuário, e realize uma contagem de 1 até esse numero (ele incluso).

n = int(input('Digite um número positivo para contar: '))
contador = 1

while contador <= n:
    print(contador, end=' ')
    contador += 1