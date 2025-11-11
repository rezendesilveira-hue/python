#Crie um programa que peça 10 numeros, e armazene-os em duas listas: `pares` e `impares`. 
#Ao final mostre as duas listas.

par = []
impar = []
qtde = 10

for numero in range(qtde):
    num_novo = int(input(f'Digite o {numero +1}º numero: '))
    
    if num_novo %2 == 0:
        par.append(num_novo)
    else:
        impar.append(num_novo)
print(f'{par}')
print(f'{impar}')

    
    
    