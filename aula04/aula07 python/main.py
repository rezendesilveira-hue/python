lista_compras = [
    {"categoria": "Hortifruti", "itens": ["Maçã", "Banana", "Alface"]},
    {"categoria": "Limpeza", "itens": ["Detergente", "Sabão em Pó", "Álcool"]},
    {"categoria": "Padaria", "itens": ["Pão de Sal", "Queijo", "Presunto"]},
    {"categoria": "Açougue", "itens": ["Patinho", "Frango", "Linguiça"]},
    {"categoria": "Bebidas", "itens": ["Água Mineral", "Suco de Uva", "Café"]}
]
print(f"{' LISTA DE SUPERMERCADO ':=^40}")

# Primeiro 'for': Extrai cada dicionário da lista principal
for secao in lista_compras:
    print(f"\n🛒 SEÇÃO: {secao['categoria'].upper()}")
    
    # Segundo 'for': Percorre a lista de itens dentro do dicionário atual
    for produto in secao['itens']:
        print(f"  • {produto}")

print("\n" + "="*40)