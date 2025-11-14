#feito via gemini
import math

# --- 1. ENTRADA DE DADOS ---

print("===================================================")
print("             CALCULADORA E ANALISADOR")
print("===================================================")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
except ValueError:
    print("\nERRO: Por favor, digite apenas números válidos.")
    exit()

print("\n--- OPERAÇÕES DISPONÍVEIS ---")
print("[+] Adição")
print("[-] Subtração")
print("[*] Multiplicação")
print("[/] Divisão")
operacao = input("Qual operação deseja realizar? ")

# --- 2. EXECUÇÃO DA OPERAÇÃO ---

resultado = None # Inicializa a variável resultado

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    # Previne a divisão por zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("\nERRO: Divisão por zero não é permitida.")
        exit()
else:
    print("\nERRO: Operação inválida. Tente novamente.")
    exit()

# --- 3. ANÁLISE DO RESULTADO ---

print("\n===================================================")
print(f"O resultado da operação é: {resultado}")
print("===================================================")

# Variável para armazenar as classificações
classificacao = ""

# A. PAR OU ÍMPAR (Só se aplica se o resultado for inteiro)
# Usamos math.trunc para checar se o número tem parte decimal
if resultado == math.trunc(resultado):
    # Se for inteiro, verifica-se par ou ímpar
    if resultado % 2 == 0:
        classificacao += "O resultado é **PAR**.\n"
    else:
        classificacao += "O resultado é **ÍMPAR**.\n"
else:
    # Se for decimal, não se classifica como par ou ímpar
    classificacao += "Não é par ou ímpar (é decimal).\n"


# B. POSITIVO OU NEGATIVO
if resultado > 0:
    classificacao += "O resultado é **POSITIVO**.\n"
elif resultado < 0:
    classificacao += "O resultado é **NEGATIVO**.\n"
else:
    # Caso o resultado seja zero
    classificacao += "O resultado é **NEUTRO** (Zero).\n"


# C. INTEIRO OU DECIMAL
if resultado == math.trunc(resultado):
    classificacao += "O resultado é um número **INTEIRO**.\n"
else:
    classificacao += "O resultado é um número **DECIMAL**.\n"


# --- 4. SAÍDA FINAL ---

print("ANÁLISE DO RESULTADO:")
print(classificacao)
print("===================================================")


