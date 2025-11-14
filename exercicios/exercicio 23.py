import math # Importa a biblioteca para usar math.trunc

# 1. Entrada de Dados (Sempre como float para aceitar decimais)
numero = float(input("Digite um número: "))

# 2. Utilização da função de arredondamento (truncamento)
# math.trunc() pega a parte inteira e ignora o que está depois da vírgula.
parte_inteira = math.trunc(numero)

# 3. Verificação Condicional
# Se o número original for igual à sua versão truncada, é inteiro.
# Caso contrário, ele tinha uma parte decimal que foi cortada.
if numero == parte_inteira:
    print(f"O número {numero} é **INTEIRO**.")
else:
    print(f"O número {numero} é **DECIMAL**.")