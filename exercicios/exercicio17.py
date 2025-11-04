 #Feito via Gemini

import math

# --- 1. DEFINIÇÃO DAS CONSTANTES ---
# Cobertura
COBERTURA_POR_LITRO = 6.0 # m² por litro

# Latas de 18 Litros
LATA_CAPACIDADE = 18.0
LATA_PRECO = 80.0

# Galões de 3,6 Litros
GALAO_CAPACIDADE = 3.6
GALAO_PRECO = 25.0

# Fator de Folga (10%)
FATOR_FOLGA = 1.10

# --- FUNÇÕES DE CÁLCULO PARA AS 3 SITUAÇÕES ---

def calcular_apenas_latas(litros_necessarios):
    """Calcula a compra usando apenas latas de 18L."""
    latas = math.ceil(litros_necessarios / LATA_CAPACIDADE)
    preco = latas * LATA_PRECO
    return latas, preco

def calcular_apenas_galao(litros_necessarios):
    """Calcula a compra usando apenas galões de 3,6L."""
    galoes = math.ceil(litros_necessarios / GALAO_CAPACIDADE)
    preco = galoes * GALAO_PRECO
    return galoes, preco

def calcular_mistura_otimizada(litros_necessarios):
    """Calcula a compra otimizada com latas e galões para menor desperdício."""

    # 1. Calcule a quantidade de latas cheias necessárias
    latas = math.floor(litros_necessarios / LATA_CAPACIDADE)
    
    # 2. Calcule o volume de tinta que *restou* após comprar as latas cheias
    litros_restantes = litros_necessarios % LATA_CAPACIDADE

    galoes = 0
    
    # 3. Se houver litros restantes, calculamos os galões
    if litros_restantes > 0:
        # Se o resto for menor que a capacidade de um galão, ainda precisamos de 1 galão.
        if litros_restantes <= GALAO_CAPACIDADE:
             galoes = 1
        # Se o resto for maior que um galão, calculamos quantos galões cheios
        else:
             galoes = math.ceil(litros_restantes / GALAO_CAPACIDADE)
             
    # Cálculo final do preço
    preco_latas = latas * LATA_PRECO
    preco_galoes = galoes * GALAO_PRECO
    preco_total = preco_latas + preco_galoes
    
    return latas, galoes, preco_total

# --- PROGRAMA PRINCIPAL ---

# 2. Entrada de Dados
try:
    area_m2 = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
    exit()

# 3. Cálculo da necessidade de tinta (com folga de 10%)
litros_brutos = area_m2 / COBERTURA_POR_LITRO
litros_com_folga = litros_brutos * FATOR_FOLGA

print("\n" + "="*55)
print(f"Área a ser pintada: {area_m2:.2f} m²")
print(f"Litros necessários (com 10% de folga): {litros_com_folga:.2f} L")
print("="*55)
print("     OPÇÕES DE COMPRA (Arredondamento sempre para cima)")
print("="*55)


# SITUAÇÃO 1: Apenas Latas de 18L
latas_1, preco_1 = calcular_apenas_latas(litros_com_folga)
print(f"1. APENAS LATAS DE 18L:")
print(f"   - Quantidade: {latas_1} lata(s)")
print(f"   - Preço Total: R$ {preco_1:.2f}\n")


# SITUAÇÃO 2: Apenas Galões de 3,6L
galoes_2, preco_2 = calcular_apenas_galao(litros_com_folga)
print(f"2. APENAS GALÕES DE 3,6L:")
print(f"   - Quantidade: {galoes_2} galão(ões)")
print(f"   - Preço Total: R$ {preco_2:.2f}\n")


# SITUAÇÃO 3: Mistura Otimizada (Menor Desperdício)
latas_3, galoes_3, preco_3 = calcular_mistura_otimizada(litros_com_folga)
print(f"3. MISTURA OTIMIZADA (Lata + Galão):")
print(f"   - Latas de 18L: {latas_3}")
print(f"   - Galões de 3,6L: {galoes_3}")
print(f"   - Preço Total: R$ {preco_3:.2f}")

print("="*55)
