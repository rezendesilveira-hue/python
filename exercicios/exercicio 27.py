#feito via gemini
# --- Tabela de Preços ---
PRECOS = {
    'morango': {'ate_5kg': 2.50, 'acima_5kg': 2.20},
    'maca': {'ate_5kg': 1.80, 'acima_5kg': 1.50}
}
LIMITE_DESCONTO_KG = 8.0  # Limite de peso para 10% de desconto
LIMITE_DESCONTO_VALOR = 25.0 # Limite de valor para 10% de desconto
TAXA_DESCONTO = 0.10 # 10%

# --- 1. ENTRADA DE DADOS ---
try:
    morango_kg = float(input("Digite a quantidade de Morangos (em Kg): "))
    maca_kg = float(input("Digite a quantidade de Maçãs (em Kg): "))
except ValueError:
    print("\nERRO: Por favor, digite apenas números válidos para o peso.")
    exit()

# --- 2. CÁLCULO DO PREÇO BRUTO (Sem desconto) ---

# CÁLCULO DO MORANGO
if morango_kg <= 5:
    preco_morango = morango_kg * PRECOS['morango']['ate_5kg']
else:
    preco_morango = morango_kg * PRECOS['morango']['acima_5kg']

# CÁLCULO DA MAÇÃ
if maca_kg <= 5:
    preco_maca = maca_kg * PRECOS['maca']['ate_5kg']
else:
    preco_maca = maca_kg * PRECOS['maca']['acima_5kg']

# CÁLCULO TOTAL
valor_bruto = preco_morango + preco_maca
peso_total = morango_kg + maca_kg

# --- 3. APLICAÇÃO DO DESCONTO ---

valor_final = valor_bruto
tem_desconto = False # Variável de controle

# Verifica se a condição de desconto é atendida
if peso_total > LIMITE_DESCONTO_KG or valor_bruto > LIMITE_DESCONTO_VALOR:
    
    valor_desconto = valor_bruto * TAXA_DESCONTO
    valor_final = valor_bruto - valor_desconto
    tem_desconto = True

# --- 4. SAÍDA DE DADOS ---

print("\n=======================================================")
print("             RESUMO DA COMPRA")
print("=======================================================")
print(f"Peso Total Adquirido: {peso_total:.2f} Kg")
print(f"Valor Bruto da Compra: R$ {valor_bruto:.2f}")

if tem_desconto:
    print("STATUS: DESCONTO DE 10% APLICADO!")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
else:
    print("STATUS: Sem desconto aplicado.")

print("-------------------------------------------------------")
print(f"VALOR TOTAL A PAGAR: R$ {valor_final:.2f}")
print("=======================================================")