#feito via gemini
litros = float(input('Digite a quantidade de litros: '))
tipo_combustivel = input('Digite o tipo do combustivel (A - Álcool / G - Gasolina): ').lower()

# Valores fixos
desc_alcool = 0.03  # 3%
desc_alcool2 = 0.05 # 5%
desc_gasolina = 0.04 # 4%
desc_gasolina2 = 0.06 # 6%
vlr_alcool = 1.90
vlr_gasolina = 2.50

# Variáveis para cálculo
total_a_pagar = 0
vlr_desconto = 0

# --- LÓGICA DE CÁLCULO ---

# BLOCÃO 1: ÁLCOOL (A)
if tipo_combustivel == 'a':
    total_alcool_bruto = litros * vlr_alcool
    
    if litros <= 20:
        # Álcool: até 20 litros, 3% de desconto
        vlr_desconto = total_alcool_bruto * desc_alcool
    else:
        # Álcool: acima de 20 litros, 5% de desconto
        vlr_desconto = total_alcool_bruto * desc_alcool2
        
    total_a_pagar = total_alcool_bruto - vlr_desconto

# BLOCÃO 2: GASOLINA (G)
elif tipo_combustivel == 'g':
    total_gasolina_bruto = litros * vlr_gasolina
    
    if litros <= 20:
        # Gasolina: até 20 litros, 4% de desconto
        vlr_desconto = total_gasolina_bruto * desc_gasolina
    else:
        # Gasolina: acima de 20 litros, 6% de desconto
        # CORREÇÃO: Usando desc_gasolina2 (0.06)
        vlr_desconto = total_gasolina_bruto * desc_gasolina2
        
    total_a_pagar = total_gasolina_bruto - vlr_desconto

# BLOCÃO 3: OUTROS TIPOS
else:
    print("\nERRO: Tipo de combustível inválido. Digite 'A' ou 'G'.")
    exit()

# --- SAÍDA FINAL ---

print("\n===================================================")
print(f"Tipo de Combustível: {tipo_combustivel.upper()}")
print(f"Litros Abastecidos: {litros:.2f} L")
print(f"Valor do Desconto: R$ {vlr_desconto:.2f}")
print(f"Total a ser pago: R$ {total_a_pagar:.2f}")
print("===================================================")
