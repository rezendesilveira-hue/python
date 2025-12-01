def apresentacao(nome, sobrenome = ''):
    print(f"Meu nome é: {nome} {sobrenome}")

apresentacao('Ana')
apresentacao('Ricardo', 'Rezende')

nome_usuario = input('Digite o nome do usuário: ')
apresentacao(nome_usuario)
