produto1 = float(input('Digite o valor do primeiro produto: '))
produto2 = float(input('Digite o valor do segundo produto: '))
produto3 = float(input('Digite o valor do terceiro produto: '))

if produto1 < produto2 and produto1 < produto3:
    print(f'O produto a ser comprado será: {produto1}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'o Produto a ser comprado será: {produto2}')
else:
    print(f'O produto a ser comprado será: {produto3}')