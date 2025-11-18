frutas = {}

while True:
    nome = input('Digite a fruta: ')
    preco = float(input('input(digite o preço: '))
    frutas[nome] = preco
    resp = input('Deseja continuar?  [S/N]')
    if resp.upper() == 'N':
        break
    
#for chave in frutas:
#    print(chave, frutas[chave])

#percorrer itens
print('Frutas cadastradas: ')
for fruta, preco in frutas.items():
    print(f' - {fruta}: R${preco:.2f}')
    
    
