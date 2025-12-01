def detalhes_produto(nome, preco, quantidade):
    preco_formatado = f'R${preco:_.2f}'
    preco_formatado = (
        preco_formatado.replace('.' , ',').replace('_' , '.')
    )
    print(f'{nome} -> Preço: R${preco_formatado} -> {quantidade} Unidades')

detalhes_produto('Notebook', 3500,  2)
