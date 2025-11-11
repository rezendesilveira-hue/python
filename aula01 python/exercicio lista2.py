#Crie uma lista vazia chamada `nomes`.
#Peça para o usuário digitar 3 nomes e adicione cada um deles à lista. Mostre a lista final.
nomes = []
qtde = 3
for nome in range(qtde):
    nome_novo = input(f'Digite o {nome + 1}º nome: ')
    nomes.append(nome_novo)
print(nomes)    
