despesas = []

while True:
    print('============================')
    print('Gerenciador de despesas     ')
    print('============================')
    print('[1] - Listar despesas')
    print('[2] - Cadastrar despesa')
    print('[3] - Editar despesa')
    print('[4] - Excluir despesa')
    print('[5] - Sair')
    print('============================')
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        if len(despesas) == 0:
            print( ' Não a despesas cadastradas')
            continue
        for despesa in despesas:
            print(f' - {despesa['Titulo']}')
            print(f' - Valor: R$: {despesa['Descricao']}')
            print(f' - Descrição:  {despesa['Descrição']}')      
        print(despesas)
    elif opcao == 2:
        titulo = input('Digite o titulo: ')
        valor = float(input('Digite o valor: R$ '))
        descricao = input('Digite a descrição: ') 
        despesa = {
            'Titulo' : titulo,
            'Valor' : valor,
            'Descrição' : descricao
        }
        despesas.append(despesa)  
        print('Despesa cadastrada com sucesso')    
    elif opcao == 3:   
        print('Despesas ')     
        i = 0
        for despesa in despesas:
            print(f'[{i}] - {despesa['Titulo']}')
            i += 1
        i - int(input('Isira a despesa: '))
        despesa = despesas[i]
        despesa['Titulo'] = input('Digite o novo titulo: ')
        despesa['Valor'] = float(input('Digite o novo valor: '))
        despesa['Descrição'] = input('Digite a nova descrição: ')
    elif opcao == 4:
        print('Despesas ')     
        i = 0
        for despesa in despesas:
            print(f'[{i}] - {despesa['Titulo']}')
            i += 1
        i - int(input('Digite a despesa que quer excluir: '))
        despesa.pop[i]
    elif opcao == 5:
        break
    else:
        print('Opcção invalida ')
print('Fim do prograna')
        
        

