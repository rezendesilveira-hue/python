#feito via chatGPT
#Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a 
# valor do saque e depois informar quantas notas de cada valor serão fornecidas. As 
# notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e 
# o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
# existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
# uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

# Notas disponíveis (em ordem decrescente)
NOTAS = [100, 50, 10, 5, 1]
VALOR_MINIMO = 10
VALOR_MAXIMO = 600

print("=====================================================")
print("      CAIXA ELETRÔNICO - SAQUE R$ 10 a R$ 600")
print("=====================================================")

try:
    # 1. Entrada de Dados
    valor_saque = int(input("Digite o valor do saque (apenas números inteiros): R$ "))
    
except ValueError:
    print("\nERRO: Por favor, digite um valor numérico inteiro.")
    exit()

# 2. Validação do Valor
if valor_saque < VALOR_MINIMO or valor_saque > VALOR_MAXIMO:
    print(f"\nERRO: O valor mínimo de saque é R$ {VALOR_MINIMO} e o máximo é R$ {VALOR_MAXIMO}.")
elif valor_saque % 1 != 0:
    print("\nERRO: O caixa eletrônico só fornece notas inteiras.")
elif valor_saque < 10: # Garante que haja notas de 10
    print("\nERRO: O valor mínimo é R$ 10.")
else:
    # 3. Processamento do Saque
    
    # O valor restante será atualizado a cada cálculo
    valor_restante = valor_saque
    
    print("\n=====================================================")
    print(f"Para o saque de R$ {valor_saque}, serão fornecidas:")
    print("=====================================================")

    # Dicionário para armazenar o resultado final
    notas_fornecidas = {} 

    # Loop para processar cada nota da maior para a menor
    for nota in NOTAS:
        # A. Divisão Inteira (//) para saber quantas notas cabem no valor restante
        quantidade_notas = valor_restante // nota
        
        # B. Se houver notas a fornecer, armazena a quantidade
        if quantidade_notas > 0:
            notas_fornecidas[nota] = quantidade_notas
            
            # C. Módulo (%) para calcular o valor que sobrou (o novo restante)
            valor_restante = valor_restante % nota
            
    # 4. Saída do Resultado
    for nota, quantidade in notas_fornecidas.items():
        print(f"  {quantidade} nota(s) de R$ {nota},00")
        
    print("=====================================================")
 