cobertura_litro = 3
capacidade_lata = 18
preco_lata = 80
m2 = float(input('Digite o metro quadrado a ser pintado: '))
litros_necessarios = m2 / cobertura_litro  
latas = litros_necessarios / capacidade_lata
preco_total = latas * preco_lata
print(f'Area a ser pintada: {m2 :.2f}')
print(f'Total de litros de tinta necessária: {litros_necessarios :.2f}')  
print(f'Quantidade de latas a serem compradas {latas :.2f}') 
print(f'Preço a pagar: {preco_total :.2f}')